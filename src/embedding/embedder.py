import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from src.config.settings import settings
from src.crawler.logger import logger

class Embedder:
    def __init__(self, model_name: str = None):
        self.model_name = model_name or settings.EMBEDDING_MODEL_NAME
        self.model = None
        self._load_model()

    def _load_model(self):
        """Load SentenceTransformer model."""
        try:
            logger.info(f"Loading embedding model: {self.model_name}...")
            # Run model on CPU to ensure safety on low memory/free-tier
            self.model = SentenceTransformer(self.model_name, device="cpu")
            logger.info("Embedding model loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading embedding model {self.model_name}: {e}")
            raise e

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for a list of texts.
        Returns a numpy array of shape (num_texts, embedding_dim).
        """
        if not texts:
            return np.empty((0, 0))
        
        try:
            # Convert to list if it's a single string
            if isinstance(texts, str):
                texts = [texts]
            
            embeddings = self.model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise e

    def embed_query(self, query: str) -> np.ndarray:
        """
        Generate embedding for a single query.
        Returns a 1D numpy array.
        """
        embeddings = self.embed_texts([query])
        return embeddings[0] if len(embeddings) > 0 else np.array([])
