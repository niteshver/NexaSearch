import hashlib
from pathlib import Path
from typing import Set
import json


class URLDeduplicator:
    """Track URLs/content hashes to skip duplicate crawls upstream."""
    
    def __init__(self, cache_file: Path = Path("data/.url_cache.json")):
        self.cache_file = cache_file
        self.seen_hashes: Set[str] = set()
        self.url_to_hash: dict = {}
        self.load_cache()
    
    def load_cache(self) -> None:
        """Load previously seen content hashes."""
        if self.cache_file.exists():
            data = json.loads(self.cache_file.read_text())
            self.seen_hashes = set(data.get("hashes", []))
            self.url_to_hash = data.get("url_to_hash", {})
    
    def save_cache(self) -> None:
        """Persist content hashes for next run."""
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        self.cache_file.write_text(json.dumps({
            "hashes": list(self.seen_hashes),
            "url_to_hash": self.url_to_hash
        }))
    
    def get_content_hash(self, content: bytes | str) -> str:
        """Hash content (file or URL response body)."""
        if isinstance(content, str):
            content = content.encode("utf-8")
        return hashlib.sha256(content).hexdigest()
    
    def is_duplicate(self, content: bytes | str, url: str = "") -> bool:
        """Check if content was already crawled."""
        content_hash = self.get_content_hash(content)
        if content_hash in self.seen_hashes:
            return True
        
        # First time seeing this content
        self.seen_hashes.add(content_hash)
        if url:
            self.url_to_hash[url] = content_hash
        return False
    
    def clear_cache(self) -> None:
        """Clear all cached hashes (full re-crawl)."""
        self.seen_hashes.clear()
        self.url_to_hash.clear()
        if self.cache_file.exists():
            self.cache_file.unlink()
