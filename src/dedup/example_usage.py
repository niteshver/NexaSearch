"""
Example: Integrating URL deduplication into your crawler.

When fetching pages, check if content already exists before processing.
"""
from src.dedup.url_dedup import URLDeduplicator

# Initialize once
dedup = URLDeduplicator()

def crawl_page(url: str, content: bytes) -> bool:
    """
    Crawl a page, skipping duplicates.
    
    Returns:
        True if content is new, False if duplicate.
    """
    if dedup.is_duplicate(content, url=url):
        print(f"⊘ Skipping duplicate: {url}")
        return False
    
    print(f"✓ Processing new content: {url}")
    # Process content...
    
    # Save cache after each batch
    dedup.save_cache()
    return True


if __name__ == "__main__":
    # Example URLs
    urls = [
        ("https://example.com/page1", b"Content A"),
        ("https://example.com/page2", b"Content A"),  # Duplicate
        ("https://example.com/page3", b"Content B"),
    ]
    
    for url, content in urls:
        crawl_page(url, content)
    
    print(f"\nTotal unique content seen: {len(dedup.seen_hashes)}")
    print(f"Cache file: {dedup.cache_file}")
