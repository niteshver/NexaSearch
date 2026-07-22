import os
import pickle
import re
from typing import List, Dict, Any, Tuple
from rank_bm25 import BM25Okapi
from src.config.settings import settings
from src.crawler.logger import logger

class BM25Index:
    def __init__(self):
        self.bm25 = None
        self.chunks: List[Dict[str, Any]] = []
        self.tokenized_corpus: List[List[str]] = []
        
        # Stop words for tokenization
        self.stop_words = {
            'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'arent', 'as', 
            'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'cant', 'cannot', 
            'could', 'couldnt', 'did', 'didnt', 'do', 'does', 'doesnt', 'doing', 'dont', 'down', 'during', 'each', 'few', 
            'for', 'from', 'further', 'had', 'hadnt', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 'hed', 'hell', 
            'hes', 'her', 'here', 'heres', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'hows', 'i', 'id', 'ill', 
            'im', 'ive', 'if', 'in', 'into', 'is', 'isnt', 'it', 'its', 'itself', 'lets', 'me', 'more', 'most', 'mustnt', 
            'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 
            'ourselves', 'out', 'over', 'own', 'same', 'shant', 'she', 'shed', 'shell', 'shes', 'should', 'shouldnt', 'so', 
            'some', 'such', 'than', 'that', 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 
            'theres', 'these', 'they', 'theyd', 'theyll', 'theyre', 'theyve', 'this', 'those', 'through', 'to', 'too', 
            'under', 'until', 'up', 'very', 'was', 'wasnt', 'we', 'wed', 'well', 'were', 'weve', 'werent', 'what', 'whats', 
            'when', 'whens', 'where', 'wheres', 'which', 'while', 'who', 'whos', 'whom', 'why', 'whys', 'with', 'wont', 
            'would', 'wouldnt', 'you', 'youd', 'youll', 'youre', 'youve', 'your', 'yours', 'yourself', 'yourselves'
        }

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize text: lowercase, strip punctuation, remove stop words.
        """
        if not text:
            return []
        
        # Lowercase and clean punctuation
        cleaned = re.sub(r'[^\w\s]', ' ', text.lower())
        tokens = cleaned.split()
        
        # Filter stop words and short tokens
        return [t for t in tokens if t not in self.stop_words and len(t) > 1]

    def index_documents(self, chunks: List[Dict[str, Any]]):
        """
        Build BM25 index on document chunks.
        """
        if not chunks:
            logger.warning("No chunks provided to build BM25 index.")
            return

        self.chunks = chunks
        self.tokenized_corpus = [self.tokenize(c.get("text", "")) for c in chunks]
        
        # Build index
        logger.info(f"Building BM25 index for {len(chunks)} chunks...")
        self.bm25 = BM25Okapi(self.tokenized_corpus)
        logger.info("BM25 index built successfully.")

    def search(self, query: str, top_k: int = 10) -> List[Tuple[Dict[str, Any], float]]:
        """
        Search the BM25 index.
        Returns a list of tuples: (chunk_dict, score)
        """
        if not self.bm25 or not self.chunks:
            return []

        tokenized_query = self.tokenize(query)
        if not tokenized_query:
            return []

        # Get scores
        scores = self.bm25.get_scores(tokenized_query)
        
        # Pair chunk and score
        ranked_results = []
        for idx, score in enumerate(scores):
            if score > 0.0:  # Only return matching documents
                ranked_results.append((self.chunks[idx], float(score)))

        # BM25Okapi assigns zero IDF in very small corpora. Preserve exact
        # token matches so a one-document index remains searchable.
        if not ranked_results:
            query_tokens = set(tokenized_query)
            ranked_results = [
                (self.chunks[idx], float(score))
                for idx, score in enumerate(scores)
                if query_tokens.intersection(self.tokenized_corpus[idx])
            ]

        # Sort by score descending
        ranked_results.sort(key=lambda x: x[1], reverse=True)
        return ranked_results[:top_k]

    def save(self, dir_path: str = None):
        """
        Save index to disk.
        """
        path = dir_path or str(settings.absolute_index_dir)
        os.makedirs(path, exist_ok=True)
        
        file_path = os.path.join(path, "bm25_index.pkl")
        try:
            with open(file_path, "wb") as f:
                pickle.dump({
                    "chunks": self.chunks,
                    "tokenized_corpus": self.tokenized_corpus
                }, f)
            logger.info(f"Saved BM25 index to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save BM25 index: {e}")

    def load(self, dir_path: str = None) -> bool:
        """
        Load index from disk.
        """
        path = dir_path or str(settings.absolute_index_dir)
        file_path = os.path.join(path, "bm25_index.pkl")
        
        if not os.path.exists(file_path):
            logger.warning(f"No BM25 index found at {file_path}")
            return False

        try:
            with open(file_path, "rb") as f:
                data = pickle.load(f)
                self.chunks = data.get("chunks", [])
                self.tokenized_corpus = data.get("tokenized_corpus", [])
            
            if self.tokenized_corpus:
                self.bm25 = BM25Okapi(self.tokenized_corpus)
                logger.info(f"Loaded BM25 index with {len(self.chunks)} chunks.")
                return True
        except Exception as e:
            logger.error(f"Failed to load BM25 index: {e}")
        
        return False
