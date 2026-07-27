from crawl4ai import SeedingConfig

"""
Per-source seeding configurations
Define unique SeedingConfig for each source/domain
"""

SOURCES = {

    'pypi.org': {

        'source': 'sitemap',
        'pattern': '*/project/*',  # Only PyPI projects
        'extract_head': True,
        'max_urls': 5000,
        'concurrency': 15,
        'hits_per_sec': 8,
        'use_bm25': True,
        'query': 'python package library',
        'score_threshold': 0.4
    },

    'arxiv.org': {
        'source': 'sitemap+cc',
        'pattern': '*/abs/*',  # Only arXiv abstracts
        'extract_head': True,
        'max_urls': 1000,
        'concurrency': 20,
        'hits_per_sec': 10,
        'use_bm25': True,
        'query': 'machine learning AI research',
        'score_threshold': 0.5,
        'live_check': True
    },
    'github.com': {
        'source': 'cc',  # Common Crawl only (no sitemap)
        'pattern': '*/blob/*',  # Only code files
        'extract_head': True,
        'max_urls': 2000,
        'concurrency': 25,
        'hits_per_sec': 15,
        'use_bm25': False,
        'filter_nonsense_urls': True
    }
}

def get_source_config(domain: str) -> dict:
    """
    Get per-source configuration for a domain.
    Returns merged config (per-source + defaults).
    
    Args:
        domain: Domain name
        
    Returns:
        Configuration dictionary
    """
    defaults = {
        'source': 'sitemap+cc',
        'pattern': '*',
        'extract_head': True,
        'max_urls': 10000,
        'concurrency': 20,
        'hits_per_sec': 10,
        'live_check': False,
        'force': False,
        'filter_nonsense_urls': True,
        'cache_ttl_hours': 24,
        'use_bm25': True,
        'query': None,
        'score_threshold': 0.3
    }
    
    # Merge with per-source config
    if domain in SOURCES:
        return {**defaults, **SOURCES[domain]}
    
    return defaults