import re
from typing import List, Dict, Tuple, Any
from src.config.settings import settings
from src.crawler.logger import logger

class QualityFilter:
    def __init__(self, threshold: float = None, min_words: int = None, max_words: int = None):
        self.threshold = threshold or settings.QUALITY_THRESHOLD
        self.min_words = min_words or settings.MIN_WORD_COUNT
        self.max_words = max_words or settings.MAX_WORD_COUNT
        self.use_ml = settings.USE_DISTILBERT_CLASSIFIER
        self.classifier = None

        # Common spam patterns
        self.spam_patterns = [
            re.compile(r'\b(click here|buy now|free shipping|make money online|online casino|slot machine|cheap pharmacy|viagra|cialis)\b', re.IGNORECASE),
            re.compile(r'\b(work from home|get rich quick|passive income|unsecured debt|forex trading|crypto lottery)\b', re.IGNORECASE)
        ]

    def load_classifier(self):
        """Lazy load the DistilBERT model if required."""
        if self.classifier is None and self.use_ml:
            try:
                from transformers import pipeline
                logger.info("Loading DistilBERT quality classification model...")
                # Use a lightweight sentiment/quality classifier
                self.classifier = pipeline("text-classification", model="distilbert/distilroberta-base", device=-1)
            except Exception as e:
                logger.error(f"Failed to load DistilBERT model: {e}. Falling back to heuristics.")
                self.use_ml = False

    def evaluate_quality(self, text: str) -> float:
        """
        Evaluate document quality score between 0.0 and 1.0.
        Uses heuristics (readability, coherence, spam) and optional ML.
        """
        if not text:
            return 0.0

        words = text.split()
        word_count = len(words)

        # 1. Length constraint check
        if word_count < self.min_words or word_count > self.max_words:
            return 0.0

        # 2. Heuristics calculation
        # A. Readability / Structural signals
        # Average word length
        avg_word_len = sum(len(w) for w in words) / word_count if word_count > 0 else 0
        word_len_score = 1.0 if 4.0 <= avg_word_len <= 8.0 else 0.4
        
        # Sentence structure (sentences end with punctuation)
        sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
        sentence_count = len(sentences)
        avg_sentence_len = word_count / sentence_count if sentence_count > 0 else 0
        sentence_score = 1.0 if 8.0 <= avg_sentence_len <= 35.0 else 0.5

        # B. Coherence / Keyword stuffing detector
        # Count frequency of top words
        word_freq = {}
        for w in words:
            w_low = w.lower()
            if len(w_low) > 3:  # Only count content words
                word_freq[w_low] = word_freq.get(w_low, 0) + 1
        
        max_freq = max(word_freq.values()) if word_freq else 0
        stuffing_ratio = max_freq / word_count if word_count > 0 else 0
        coherence_score = 1.0
        if stuffing_ratio > 0.08:  # Word stuffing penalty
            coherence_score = max(0.0, 1.0 - (stuffing_ratio - 0.08) * 10)

        # C. Spam check
        spam_hits = 0
        for pattern in self.spam_patterns:
            spam_hits += len(pattern.findall(text))
        
        spam_score = max(0.0, 1.0 - (spam_hits * 0.2))

        # Combine heuristics
        heuristic_score = (0.3 * word_len_score) + (0.3 * sentence_score) + (0.2 * coherence_score) + (0.2 * spam_score)

        # 3. Optional ML Classifier
        if self.use_ml:
            self.load_classifier()
            if self.classifier:
                try:
                    # Truncate text to model input size (typically 512 tokens)
                    truncated_text = " ".join(words[:400])
                    result = self.classifier(truncated_text)[0]
                    # Score based on label (assume positive label indicates higher quality)
                    ml_score = result.get('score', 0.5) if result.get('label') == 'LABEL_1' else 1.0 - result.get('score', 0.5)
                    # Weighted combination
                    return 0.5 * heuristic_score + 0.5 * ml_score
                except Exception as e:
                    logger.warning(f"Error executing classifier: {e}. Defaulting to heuristic score.")
        
        return heuristic_score

    def filter_documents(self, documents: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Filter a batch of documents, keeping only those above the quality threshold.
        """
        filtered_docs = []
        stats = {
            "input_count": len(documents),
            "filtered_out": 0,
            "output_count": 0,
            "average_quality_score": 0.0
        }

        total_score = 0.0
        for doc in documents:
            text = doc.get("markdown", "") or doc.get("text", "")
            score = self.evaluate_quality(text)
            
            # Save the score in doc metadata
            if "metadata" not in doc:
                doc["metadata"] = {}
            doc["metadata"]["quality_score"] = round(score, 3)

            if score >= self.threshold:
                filtered_docs.append(doc)
                total_score += score
            else:
                stats["filtered_out"] += 1

        stats["output_count"] = len(filtered_docs)
        stats["average_quality_score"] = round(total_score / len(filtered_docs), 3) if filtered_docs else 0.0
        return filtered_docs, stats
