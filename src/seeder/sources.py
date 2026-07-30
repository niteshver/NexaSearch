from typing import List, Dict, Any

SOURCES = {
    'pypi.org': {
        'source': 'sitemap',
        'pattern': '*/project/*',  # Only PyPI projects
        'extract_head': True,
        'max_urls': 50000,
        'concurrency': 15,
        'hits_per_sec': 8,
        'use_bm25': True,
        'query': 'python package library framework',
        'score_threshold': 0.4,
        'live_check': False,
        'description': 'Python Package Index - project pages'
    },

    'arxiv.org': {
        'source': 'sitemap+cc',
        'pattern': '*/abs/*',  # Only arXiv abstracts
        'extract_head': True,
        'max_urls': 50000,
        'concurrency': 20,
        'hits_per_sec': 10,
        'use_bm25': True,
        'query': 'machine learning artificial intelligence deep learning research paper',
        'score_threshold': 0.5,
        'live_check': True,
        'description': 'arXiv Research Papers - abstracts only'
    },

    # ===== GITHUB CONFIGURATIONS =====
    'github.com': {
        'source': 'cc',  # Common Crawl (no official sitemap)
        'patterns': {
            'documentation': '*/docs/*',
            'code': '*/blob/*/*.py',  # ✓ FIXED: was */blob/*/**.py
            'research': '*/research/*',
            'papers': '*/papers/*',
            'issues': '*/issues/*',
            'pulls': '*/pull/*',
            'releases': '*/releases/*',
            'wiki': '*/wiki/*',
            'discussions': '*/discussions/*'
        },
        'extract_head': True,
        'max_urls': 100000,
        'concurrency': 30,
        'hits_per_sec': 20,
        'use_bm25': True,
        'query': 'python machine learning deep learning NLP computer vision',
        'score_threshold': 0.35,
        'live_check': False,
        'filter_nonsense_urls': True,
        'description': 'GitHub - code, docs, research, issues, PRs',
        'organizations': [
            'pytorch',
            'tensorflow',
            'langchain-ai',
            'huggingface',
            'openai',
            'anthropic',  # ✓ FIXED: was 'anthropics'
            'deepmind',
            'facebook',
            'google-research',
            'microsoft',
            'aws',
            'scikit-learn',
            'pandas-dev',
            'numpy',
            'torchvision',
            'scikit-image'
        ]
    },

    'pytorch.org': {
        'source': 'sitemap+cc',
        'pattern': '*/tutorials/*',  # PyTorch tutorials
        'extract_head': True,
        'max_urls': 5000,
        'concurrency': 20,
        'hits_per_sec': 12,
        'use_bm25': True,
        'query': 'deep learning neural network PyTorch tutorial documentation',
        'score_threshold': 0.4,
        'live_check': True,
        'description': 'PyTorch - tutorials and documentation'
    },

    'docs.python.org': {
        'source': 'sitemap',
        'pattern': '*/library/*',  # Python standard library docs
        'extract_head': True,
        'max_urls': 5000,
        'concurrency': 15,
        'hits_per_sec': 10,
        'use_bm25': False,  # ✓ No query needed
        'live_check': False,
        'description': 'Python Official Documentation'
    },

    'numpy.org': {
        'source': 'sitemap+cc',
        'pattern': '*/doc/*',  # NumPy documentation
        'extract_head': True,
        'max_urls': 3000,
        'concurrency': 15,
        'hits_per_sec': 10,
        'use_bm25': False,  # ✓ No query needed
        'description': 'NumPy - numerical computing library'
    },

    'pandas.org': {
        'source': 'sitemap+cc',
        'pattern': '*/docs/*',  # Pandas documentation
        'extract_head': True,
        'max_urls': 5000,
        'concurrency': 20,
        'hits_per_sec': 12,
        'use_bm25': True,
        'query': 'pandas dataframe data manipulation documentation',
        'score_threshold': 0.35,
        'description': 'Pandas - data analysis library'
    },

    'docs.opencv.org': {
        'source': 'sitemap+cc',
        'pattern': '*/modules/*',  # OpenCV modules
        'extract_head': True,
        'max_urls': 4000,
        'concurrency': 15,
        'hits_per_sec': 10,
        'use_bm25': False,  # ✓ No query needed
        'description': 'OpenCV - computer vision library'
    },

    'docs.docker.com': {
        'source': 'sitemap',
        'pattern': '*/guides/*',  # Docker guides and docs
        'extract_head': True,
        'max_urls': 3000,
        'concurrency': 15,
        'hits_per_sec': 10,
        'use_bm25': True,
        'query': 'docker container kubernetes deployment',
        'score_threshold': 0.35,
        'description': 'Docker - containerization documentation'
    },

    'kernel.org': {
        'source': 'cc',
        'pattern': '*/doc/*',  # Linux kernel docs
        'extract_head': True,
        'max_urls': 2000,
        'concurrency': 10,
        'hits_per_sec': 5,
        'use_bm25': False,
        'live_check': False,
        'description': 'Linux Kernel Documentation'
    },

    'fastapi.tiangolo.com': {
        'source': 'sitemap',
        'pattern': '*/advanced/*',  # FastAPI advanced docs
        'extract_head': True,
        'max_urls': 2000,
        'concurrency': 15,
        'hits_per_sec': 10,
        'use_bm25': True,
        'query': 'FastAPI web framework API documentation',
        'score_threshold': 0.3,
        'description': 'FastAPI - modern web framework'
    },

    'python.langchain.com': {
        'source': 'sitemap+cc',
        'pattern': '*/docs/*',  # LangChain documentation
        'extract_head': True,
        'max_urls': 3000,
        'concurrency': 15,
        'hits_per_sec': 10,
        'use_bm25': True,
        'query': 'LangChain LLM language model chain',
        'score_threshold': 0.35,
        'description': 'LangChain - LLM orchestration framework'
    },
}


class GitHubSeeder:
    """
    Specialized seeder for GitHub repositories and organizations.
    Handles multiple URL patterns (docs, code, issues, PRs, research).
    """

    GITHUB_PATTERNS = {
        'documentation': [
            '*/docs/*',
            '*/documentation/*',
            '*/guide/*',
            '*/tutorial/*',
            '*/wiki/*'
        ],
        'code': [
            '*/blob/*/*.py',      # ✓ FIXED: was */blob/*/**.py
            '*/blob/*/*.js',      # ✓ FIXED: was */blob/*/**.js
            '*/blob/*/*.java',    # ✓ FIXED: was */blob/*/**.java
            '*/blob/*/*.go',      # ✓ FIXED: was */blob/*/**.go
            '*/tree/main',
            '*/tree/master'
        ],
        'research': [
            '*/research/*',
            '*/papers/*',
            '*/publications/*',
            '*/whitepaper*'
        ],
        'issues': [
            '*/issues/*',
            '*/discussions/*'
        ],
        'pull_requests': [
            '*/pull/*',
            '*/pulls/*'
        ],
        'releases': [
            '*/releases/*',
            '*/releases/tag/*'
        ]
    }

    @staticmethod
    def get_github_patterns(content_types: List[str] = None) -> List[str]:
        """
        Get URL patterns for specific GitHub content types.

        Args:
            content_types: List of types ('documentation', 'code', 'research', 'issues', 'pull_requests', 'releases')

        Returns:
            List of URL patterns
        """
        if not content_types:
            # Return all patterns
            patterns = []
            for pattern_list in GitHubSeeder.GITHUB_PATTERNS.values():
                patterns.extend(pattern_list)
            return patterns

        patterns = []
        for content_type in content_types:
            if content_type in GitHubSeeder.GITHUB_PATTERNS:
                patterns.extend(GitHubSeeder.GITHUB_PATTERNS[content_type])

        return patterns

    @staticmethod
    def get_organization_urls(org_name: str, content_types: List[str] = None) -> List[str]:
        """
        Generate GitHub organization URLs for specific content types.

        Args:
            org_name: GitHub organization name (e.g., 'pytorch', 'tensorflow')
            content_types: List of types to include

        Returns:
            List of GitHub URLs to seed
        """
        base_url = f"https://github.com/{org_name}"

        urls = []

        content_map = {
            'repositories': f"{base_url}?tab=repositories",
            'starred': f"{base_url}?tab=stars",
            'followers': f"{base_url}/followers",
            'following': f"{base_url}/following"
        }

        if not content_types:
            return list(content_map.values())

        return [url for key, url in content_map.items() if key in content_types]


def get_source_config(domain: str) -> Dict[str, Any]:
    """
    Get per-source configuration for a domain.
    Returns merged config (per-source + defaults).
    Production-grade with validation.

    Args:
        domain: Domain name (e.g., 'github.com', 'pytorch.org')

    Returns:
        Configuration dictionary

    Raises:
        ValueError: If domain configuration is invalid
    """
    defaults = {
        'source': 'sitemap+cc',
        'pattern': '*',
        'patterns': {},  # For multiple patterns
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
        'score_threshold': 0.3,
        'description': domain
    }

    # Merge with per-source config
    if domain in SOURCES:
        source_config = SOURCES[domain]
        merged = {**defaults, **source_config}

        # Validation
        if merged['max_urls'] > 100000:
            merged['max_urls'] = 100000
            print(f"⚠️  Warning: max_urls capped at 100000 for {domain}")

        if merged['concurrency'] > 50:
            merged['concurrency'] = 50
            print(f"⚠️  Warning: concurrency capped at 50 for {domain}")

        return merged

    return defaults


def get_github_config(
    content_types: List[str] = None,
    organizations: List[str] = None,
    max_urls: int = 10000
) -> Dict[str, Any]:
    """
    Get specialized GitHub seeding configuration.

    Args:
        content_types: Types of content ('documentation', 'code', 'research', 'issues', 'pull_requests', 'releases')
        organizations: GitHub organizations to prioritize
        max_urls: Maximum URLs to discover

    Returns:
        GitHub-specific configuration
    """
    config = get_source_config('github.com').copy()

    # Add content type filtering
    if content_types:
        patterns = GitHubSeeder.get_github_patterns(content_types)
        config['github_patterns'] = patterns
        config['description'] = f"GitHub - {', '.join(content_types)}"

    # Add organization filtering
    if organizations:
        config['github_organizations'] = organizations
        config['description'] = f"GitHub organizations: {', '.join(organizations)}"

    config['max_urls'] = min(max_urls, 50000)

    return config


def validate_source_config(config: Dict[str, Any], domain: str) -> bool:
    """
    Validate source configuration.
    
    ✓ IMPROVED: Added validation for hits_per_sec and score_threshold

    Args:
        config: Configuration dictionary
        domain: Domain name

    Returns:
        True if valid

    Raises:
        ValueError: If configuration is invalid
    """
    required_fields = ['source', 'extract_head', 'max_urls', 'concurrency']

    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field '{field}' in {domain} config")

    if config['source'] not in ['sitemap', 'cc', 'sitemap+cc']:
        raise ValueError(f"Invalid source '{config['source']}' for {domain}")

    if not (1 <= config['concurrency'] <= 50):
        raise ValueError(f"Concurrency must be 1-50, got {config['concurrency']}")

    if not (1 <= config['max_urls'] <= 100000):
        raise ValueError(f"max_urls must be 1-100000, got {config['max_urls']}")

    # ✓ NEW: Validate hits_per_sec
    if 'hits_per_sec' in config and not (1 <= config['hits_per_sec'] <= 100):
        raise ValueError(f"hits_per_sec must be 1-100, got {config['hits_per_sec']}")

    # ✓ NEW: Validate score_threshold
    if 'score_threshold' in config and not (0.0 <= config['score_threshold'] <= 1.0):
        raise ValueError(f"score_threshold must be 0.0-1.0, got {config['score_threshold']}")

    # ✓ NEW: Validate BM25 + query consistency
    if config.get('use_bm25', False) and not config.get('query'):
        raise ValueError(f"BM25 enabled for {domain} but no query provided")

    return True


# ✓ IMPROVED: Example usage with error handling
if __name__ == "__main__":
    try:
        # Standard domain config
        pypi_config = get_source_config('pypi.org')
        print(f"✓ PyPI Config: {pypi_config['pattern']}")

        # GitHub-specific config
        github_config = get_github_config(
            content_types=['documentation', 'code', 'research'],
            organizations=['pytorch', 'tensorflow', 'huggingface'],
            max_urls=20000
        )
        print(f"✓ GitHub Config: {github_config['description']}")

        # Validate
        validate_source_config(github_config, 'github.com')
        print("✓ Configuration valid")
        
    except ValueError as e:
        print(f"✗ Configuration Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected Error: {e}")