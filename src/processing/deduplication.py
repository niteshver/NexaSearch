import hashlib
import re
from typing import List, Dict, Set, Tuple, Any
from src.config.settings import settings
from src.crawler.utils import canonicalize_url

class DeduplicationPipeline:
    def __init__(self, jaccard_threshold: float = None, num_permutations: int = None):
        self.jaccard_threshold = jaccard_threshold or settings.JACCARD_THRESHOLD
        self.num_permutations = num_permutations or settings.NUM_PERMUTATIONS
        
        # Exact deduplication sets
        self.seen_content_hashes: Set[str] = set()
        self.seen_canonical_urls: Set[str] = set()
        
        # Near deduplication (LSH) structures
        # LSH parameters: b bands, r rows. b * r = num_permutations.
        # If threshold is 0.85, we want (1/b)^(1/r) ≈ 0.85.
        # For M = 128, b=16 and r=8 is a standard choice.
        self.b = 16
        self.r = 8
        assert self.b * self.r == self.num_permutations, "num_permutations must equal b * r"
        
        # LSH buckets: band_idx -> { bucket_hash -> [doc_id] }
        self.lsh_buckets: List[Dict[str, List[str]]] = [{} for _ in range(self.b)]
        # Map doc_id -> shingles set
        self.doc_shingles: Dict[str, Set[str]] = {}
        # Map doc_id -> signature list
        self.doc_signatures: Dict[str, List[int]] = {}
        
        # Large prime for hashing MinHash shingles
        self.prime = 4294967291  # 2^32 - 5

    def is_exact_duplicate(self, text: str, url: str) -> bool:
        """
        Check if the document is an exact duplicate by content hash or canonicalized URL.
        """
        # 1. Canonicalize URL
        canonical_url = canonicalize_url(url)
        if canonical_url in self.seen_canonical_urls:
            return True

        # 2. Content SHA256 Hash
        content_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        if content_hash in self.seen_content_hashes:
            return True

        return False

    def add_exact_hash(self, text: str, url: str):
        """Register the document as processed."""
        canonical_url = canonicalize_url(url)
        content_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        self.seen_canonical_urls.add(canonical_url)
        self.seen_content_hashes.add(content_hash)

    def get_shingles(self, text: str) -> Set[str]:
        """
        Extract word 3-grams as shingles.
        """
        # Clean text: remove non-alphanumeric and lowercase
        cleaned_text = re.sub(r'[^\w\s]', ' ', text.lower())
        words = cleaned_text.split()
        
        shingles = set()
        for i in range(len(words) - 2):
            shingle = f"{words[i]} {words[i+1]} {words[i+2]}"
            shingles.add(shingle)
        return shingles

    def get_minhash_signature(self, shingles: Set[str]) -> List[int]:
        """
        Compute MinHash signature of 128 hash values.
        """
        if not shingles:
            return [self.prime] * self.num_permutations

        signature = [self.prime] * self.num_permutations
        
        # Hash shingles once into 32-bit integers
        shingle_hashes = []
        for shingle in shingles:
            # Create a 32-bit hash value for the shingle
            h = int(hashlib.md5(shingle.encode('utf-8')).hexdigest(), 16) % self.prime
            shingle_hashes.append(h)

        # MinHash calculation: h_i(x) = (a_i * x + b_i) % prime
        # For simplicity and speed, we can use a salt based hash function:
        # h_i(x) = hash(x + i) % prime
        for i in range(self.num_permutations):
            min_val = self.prime
            for sh_hash in shingle_hashes:
                # Simple permutation simulation using standard hashing
                val = int(hashlib.sha1(f"{sh_hash}_{i}".encode('utf-8')).hexdigest(), 16) % self.prime
                if val < min_val:
                    min_val = val
            signature[i] = min_val

        return signature

    def is_near_duplicate(self, doc_id: str, text: str) -> bool:
        """
        Check if the document is a near-duplicate of any already indexed document.
        """
        shingles = self.get_shingles(text)
        if not shingles:
            return False

        sig = self.get_minhash_signature(shingles)
        
        # Query LSH to find candidate doc_ids
        candidates: Set[str] = set()
        for band_idx in range(self.b):
            band_sig = tuple(sig[band_idx * self.r : (band_idx + 1) * self.r])
            bucket_hash = hashlib.md5(str(band_sig).encode('utf-8')).hexdigest()
            
            if bucket_hash in self.lsh_buckets[band_idx]:
                candidates.update(self.lsh_buckets[band_idx][bucket_hash])

        # Verify Jaccard similarity for candidates
        for candidate_id in candidates:
            cand_shingles = self.doc_shingles.get(candidate_id)
            if cand_shingles:
                intersection = len(shingles.intersection(cand_shingles))
                union = len(shingles.union(cand_shingles))
                jaccard = intersection / union if union > 0 else 0.0
                if jaccard >= self.jaccard_threshold:
                    return True

        # If it is not a duplicate, store it in our indexing structures
        self.doc_shingles[doc_id] = shingles
        self.doc_signatures[doc_id] = sig
        
        # Add to LSH buckets
        for band_idx in range(self.b):
            band_sig = tuple(sig[band_idx * self.r : (band_idx + 1) * self.r])
            bucket_hash = hashlib.md5(str(band_sig).encode('utf-8')).hexdigest()
            
            if bucket_hash not in self.lsh_buckets[band_idx]:
                self.lsh_buckets[band_idx][bucket_hash] = []
            self.lsh_buckets[band_idx][bucket_hash].append(doc_id)

        return False

    def deduplicate_batch(self, documents: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
        """
        Process a list of documents and filter out exact and near duplicates.
        """
        unique_docs = []
        stats = {
            "input_count": len(documents),
            "exact_duplicates": 0,
            "near_duplicates": 0,
            "output_count": 0
        }

        for doc in documents:
            url = doc.get("url", "")
            text = doc.get("markdown", "") or doc.get("text", "")
            doc_id = doc.get("id") or hashlib.md5(url.encode()).hexdigest()
            
            # 1. Exact check
            if self.is_exact_duplicate(text, url):
                stats["exact_duplicates"] += 1
                continue
                
            # 2. Near duplicate check
            if self.is_near_duplicate(doc_id, text):
                stats["near_duplicates"] += 1
                continue
            
            # Not duplicate, keep it!
            self.add_exact_hash(text, url)
            unique_docs.append(doc)

        stats["output_count"] = len(unique_docs)
        return unique_docs, stats
