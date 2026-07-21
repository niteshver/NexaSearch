import os
import numpy as np
from typing import List, Dict, Any, Tuple
from src.config.settings import settings
from src.crawler.logger import logger
from src.search.bm25_index import BM25Index
from src.embedding.embedder import Embedder

class SearchEngine:
    def __init__(self):
        self.bm25_index = BM25Index()
        self.embedder = Embedder()
        self.cross_encoder = None
        self.embeddings: np.ndarray = np.empty((0, 0))
        
        # Load indices if they exist
        self.load()

    def _load_cross_encoder(self):
        """Lazy load the Cross-Encoder model to save memory if not used."""
        if self.cross_encoder is None:
            try:
                from sentence_transformers import CrossEncoder
                logger.info(f"Loading Cross-Encoder model: {settings.CROSS_ENCODER_MODEL_NAME}...")
                # Run on CPU to keep memory footprint low
                self.cross_encoder = CrossEncoder(settings.CROSS_ENCODER_MODEL_NAME, device="cpu")
                logger.info("Cross-Encoder loaded successfully.")
            except Exception as e:
                logger.error(f"Failed to load Cross-Encoder: {e}. Reranking will be disabled.")
                self.cross_encoder = None

    def index(self, chunks: List[Dict[str, Any]]):
        """
        Build both BM25 and Vector indexes on chunks.
        """
        if not chunks:
            logger.warning("No chunks to index.")
            return

        # 1. Build BM25
        self.bm25_index.index_documents(chunks)

        # 2. Build Embeddings
        logger.info(f"Generating embeddings for {len(chunks)} chunks...")
        texts = [c.get("text", "") for c in chunks]
        self.embeddings = self.embedder.embed_texts(texts)
        logger.info(f"Embeddings generated with shape: {self.embeddings.shape}")
        
        # Save indices
        self.save()

    def search(self, query: str, top_k: int = 10, use_vector: bool = True, use_rerank: bool = True) -> List[Dict[str, Any]]:
        """
        Execute Hybrid Search (BM25 + Vector Search) -> RRF -> Cross-Encoder Reranking -> Quality Boost.
        """
        if not self.bm25_index.chunks:
            return []

        # 1. BM25 Search (Retrieve top 100)
        bm25_results = self.bm25_index.search(query, top_k=100)
        bm25_ranks = {res[0]["chunk_id"]: idx for idx, res in enumerate(bm25_results)}

        # 2. Vector Search (Retrieve top 100)
        vector_results = []
        if use_vector and self.embeddings.size > 0:
            query_emb = self.embedder.embed_query(query)
            if query_emb.size > 0:
                # Compute cosine similarities
                norm_embeddings = np.linalg.norm(self.embeddings, axis=1)
                norm_query = np.linalg.norm(query_emb)
                
                # Prevent division by zero
                norm_embeddings[norm_embeddings == 0] = 1.0
                norm_query = 1.0 if norm_query == 0 else norm_query
                
                similarities = np.dot(self.embeddings, query_emb) / (norm_embeddings * norm_query)
                
                # Get top 100 indices
                top_indices = np.argsort(similarities)[::-1][:100]
                for idx in top_indices:
                    sim = float(similarities[idx])
                    if sim > 0.0:  # Only matching vector similarity
                        vector_results.append((self.bm25_index.chunks[idx], sim))
        
        vector_ranks = {res[0]["chunk_id"]: idx for idx, res in enumerate(vector_results)}

        # 3. Reciprocal Rank Fusion (RRF)
        # Combines BM25 and Vector lists
        k_rrf = 60
        rrf_scores = {}
        all_matches = {}

        for chunk, _ in bm25_results:
            cid = chunk["chunk_id"]
            all_matches[cid] = chunk
            bm25_rank = bm25_ranks[cid]
            rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (k_rrf + bm25_rank))

        for chunk, _ in vector_results:
            cid = chunk["chunk_id"]
            all_matches[cid] = chunk
            vec_rank = vector_ranks[cid]
            rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (k_rrf + vec_rank))

        # Sort by RRF score descending
        sorted_rrf = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Take top 30 candidates for reranking
        candidates = [all_matches[cid] for cid, _ in sorted_rrf[:30]]
        
        if not candidates:
            return []

        # 4. Cross-Encoder Reranking
        final_scores = {}
        if use_rerank and len(candidates) > 0:
            self._load_cross_encoder()
            if self.cross_encoder:
                try:
                    pairs = [[query, cand.get("text", "")] for cand in candidates]
                    ce_scores = self.cross_encoder.predict(pairs)
                    
                    # Store scores
                    for cand, ce_score in zip(candidates, ce_scores):
                        final_scores[cand["chunk_id"]] = float(ce_score)
                except Exception as e:
                    logger.error(f"Error during Cross-Encoder rerank: {e}. Falling back to RRF.")
                    # Fallback to RRF scores
                    for cid, rrf_score in sorted_rrf[:30]:
                        final_scores[cid] = rrf_score
            else:
                # Fallback to RRF scores
                for cid, rrf_score in sorted_rrf[:30]:
                    final_scores[cid] = rrf_score
        else:
            # RRF scores as default
            for cid, rrf_score in sorted_rrf[:30]:
                final_scores[cid] = rrf_score

        # 5. Quality Boost
        # Score = normalized_score + settings.QUALITY_WEIGHT * quality_score
        # For CE scores (which are typically logits or logit-like), we can convert to range or just add quality signal
        # Let's normalize final_scores to [0, 1] range first
        max_score = max(final_scores.values()) if final_scores else 1.0
        min_score = min(final_scores.values()) if final_scores else 0.0
        score_range = max_score - min_score if max_score != min_score else 1.0

        boosted_results = []
        for cand in candidates:
            cid = cand["chunk_id"]
            raw_score = final_scores[cid]
            normalized_score = (raw_score - min_score) / score_range
            
            # Quality score (stored in metadata)
            quality_score = cand.get("metadata", {}).get("quality_score", 0.5)
            
            # Composite score
            composite_score = (normalized_score * (1.0 - settings.QUALITY_WEIGHT)) + (quality_score * settings.QUALITY_WEIGHT)
            
            boosted_results.append({
                "chunk": cand,
                "score": round(composite_score, 4)
            })

        # Sort and return top K
        boosted_results.sort(key=lambda x: x["score"], reverse=True)
        
        # Format output
        results = []
        for idx, item in enumerate(boosted_results[:top_k]):
            chunk = item["chunk"]
            # Generate snippet from text
            snippet = self._generate_snippet(chunk["text"], query)
            
            results.append({
                "rank": idx + 1,
                "chunk_id": chunk["chunk_id"],
                "doc_id": chunk["doc_id"],
                "title": chunk["title"],
                "url": chunk["url"],
                "heading": chunk["heading"],
                "snippet": snippet,
                "score": item["score"],
                "quality_score": chunk.get("metadata", {}).get("quality_score", 0.5)
            })

        return results

    def _generate_snippet(self, text: str, query: str) -> str:
        """Find the most relevant sentence or section containing query words."""
        sentences = re.split(r'(?<=[.!?])\s+', text)
        query_words = [w.lower() for w in query.split() if len(w) > 2]
        
        if not query_words:
            return text[:250] + "..." if len(text) > 250 else text

        best_sentence = ""
        max_matches = -1

        for sent in sentences:
            matches = sum(1 for w in query_words if w in sent.lower())
            if matches > max_matches:
                max_matches = matches
                best_sentence = sent

        # Highlight query terms in the snippet using bold markdown
        snippet = best_sentence or sentences[0]
        
        # Basic highlight
        for w in query_words:
            pattern = re.compile(rf'\b({re.escape(w)})\b', re.IGNORECASE)
            snippet = pattern.sub(r'**\1**', snippet)

        if len(snippet) > 250:
            snippet = snippet[:250] + "..."
        return snippet

    def save(self, dir_path: str = None):
        """Save BM25 index and embeddings to disk."""
        path = dir_path or str(settings.absolute_index_dir)
        os.makedirs(path, exist_ok=True)
        
        # Save BM25
        self.bm25_index.save(path)
        
        # Save embeddings
        if self.embeddings.size > 0:
            emb_path = os.path.join(path, "vector_index.npy")
            try:
                np.save(emb_path, self.embeddings)
                logger.info(f"Saved vector embeddings to {emb_path}")
            except Exception as e:
                logger.error(f"Failed to save embeddings: {e}")

    def load(self, dir_path: str = None) -> bool:
        """Load BM25 index and embeddings from disk."""
        path = dir_path or str(settings.absolute_index_dir)
        
        # Load BM25
        bm25_success = self.bm25_index.load(path)
        
        # Load embeddings
        emb_path = os.path.join(path, "vector_index.npy")
        embeddings_success = False
        if os.path.exists(emb_path):
            try:
                self.embeddings = np.load(emb_path)
                logger.info(f"Loaded vector embeddings with shape {self.embeddings.shape}")
                embeddings_success = True
            except Exception as e:
                logger.error(f"Failed to load embeddings: {e}")
                self.embeddings = np.empty((0, 0))

        return bm25_success and embeddings_success
