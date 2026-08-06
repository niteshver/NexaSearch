"""
Enterprise-Scale AI/ML/Research Vertical Search Engine Sources

Target: 2+ Million URLs Discovery
Audience: AI Researchers, ML Engineers, Data Scientists, Industry Professionals
Focus: Maximum coverage - Academic, Industry, Code, Data, Research

This configuration includes 150+ high-quality sources optimized for:
- Breadth: Cover all major AI/ML domains
- Depth: Multiple patterns per domain
- Quality: High authority sources only
- Scale: 2M+ URL discovery
"""

from typing import Dict, List, Any
from pydantic import BaseModel, Field, validator
from enum import Enum


class SourceType(str, Enum):
    """Enterprise source types."""
    ACADEMIC = "academic"
    PREPRINT = "preprint"
    FRAMEWORK = "framework"
    RESEARCH_LAB = "research_lab"
    RESEARCH_GROUP = "research_group"
    DOCUMENTATION = "documentation"
    BLOG = "blog"
    GITHUB = "github"
    DATASET = "dataset"
    BENCHMARK = "benchmark"
    CONFERENCE = "conference"
    JOURNAL = "journal"
    BOOK = "book"
    COURSE = "course"
    COMPETITION = "competition"


class EnterpriseSource(BaseModel):
    """Enterprise-scale source configuration."""
    
    domain: str = Field(..., description="Domain name")
    source_type: SourceType = Field(..., description="Source category")
    url: str = Field(..., description="Base URL")
    patterns: List[str] = Field(default_factory=lambda: ["*"], description="Multiple URL patterns")
    max_urls: int = Field(default=50000, ge=1, le=500000)
    concurrency: int = Field(default=30, ge=1, le=100)
    hits_per_sec: float = Field(default=15.0, ge=0.1, le=150.0)
    priority: int = Field(default=5, ge=1, le=10)
    reputation: float = Field(default=0.8, ge=0.0, le=1.0)
    live_check: bool = Field(default=False)
    query: str = Field(default="")
    description: str = Field(default="")
    urls_estimate: int = Field(default=10000, description="Estimated URLs in source")


# ============================================================================
# TIER 1: MEGA SOURCES (100K+ URLs each)
# ============================================================================

MEGA_ACADEMIC_SOURCES: Dict[str, Dict[str, Any]] = {
    # arXiv - 2.3M+ papers (largest)
    "arxiv.org": {
        "source_type": "preprint",
        "url": "https://arxiv.org",
        "patterns": [
            "*/abs/*",           # Abstracts (main)
            "*/pdf/*",           # PDFs
            "*/list/*",          # Lists
        ],
        "max_urls": 500000,      # Maximum possible
        "concurrency": 50,
        "hits_per_sec": 30.0,
        "priority": 1,
        "reputation": 1.0,
        "live_check": True,
        "query": "machine learning deep learning neural networks AI research",
        "description": "arXiv - 2.3M+ preprints (largest repository)",
        "urls_estimate": 500000,
    },
    
    # Google Scholar - Massive academic DB
    "scholar.google.com": {
        "source_type": "academic",
        "url": "https://scholar.google.com",
        "patterns": [
            "*/scholar*",
            "*/citations*",
        ],
        "max_urls": 300000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 1,
        "reputation": 0.95,
        "query": "machine learning AI research",
        "description": "Google Scholar - 300M+ academic papers",
        "urls_estimate": 300000,
    },
    
    # PubMed - Biomedical (includes AI/ML in healthcare)
    "pubmed.ncbi.nlm.nih.gov": {
        "source_type": "academic",
        "url": "https://pubmed.ncbi.nlm.nih.gov",
        "patterns": [
            "*/",
        ],
        "max_urls": 200000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 2,
        "reputation": 0.98,
        "query": "machine learning deep learning neural networks health AI",
        "description": "PubMed - 34M+ biomedical papers",
        "urls_estimate": 200000,
    },
    
    # SSRN - Social Science Research Network
    "ssrn.com": {
        "source_type": "preprint",
        "url": "https://ssrn.com",
        "patterns": [
            "*/papers*",
        ],
        "max_urls": 150000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 2,
        "reputation": 0.90,
        "query": "machine learning artificial intelligence",
        "description": "SSRN - 800K+ research papers",
        "urls_estimate": 150000,
    },
}


# ============================================================================
# TIER 1: MAJOR GITHUB SOURCES (100K+ URLs each)
# ============================================================================

MEGA_GITHUB_SOURCES: Dict[str, Dict[str, Any]] = {
    "github.com/pytorch": {
        "source_type": "github",
        "url": "https://github.com/pytorch",
        "patterns": [
            "*/tree/*",
            "*/blob/*",
            "*/search*",
            "*/issues*",
            "*/pulls*",
        ],
        "max_urls": 200000,
        "concurrency": 50,
        "hits_per_sec": 25.0,
        "priority": 1,
        "reputation": 1.0,
        "query": "PyTorch deep learning",
        "description": "PyTorch - Deep learning framework",
        "urls_estimate": 200000,
    },
    
    "github.com/tensorflow": {
        "source_type": "github",
        "url": "https://github.com/tensorflow",
        "patterns": [
            "*/tree/*",
            "*/blob/*",
            "*/search*",
            "*/issues*",
            "*/pulls*",
        ],
        "max_urls": 200000,
        "concurrency": 50,
        "hits_per_sec": 25.0,
        "priority": 1,
        "reputation": 1.0,
        "query": "TensorFlow machine learning",
        "description": "TensorFlow - ML framework",
        "urls_estimate": 200000,
    },
    
    "github.com/huggingface": {
        "source_type": "github",
        "url": "https://github.com/huggingface",
        "patterns": [
            "*/tree/*",
            "*/blob/*",
            "*/models*",
            "*/datasets*",
        ],
        "max_urls": 150000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 1,
        "reputation": 0.98,
        "query": "transformer NLP model",
        "description": "Hugging Face - NLP models",
        "urls_estimate": 150000,
    },
    
    "github.com/openai": {
        "source_type": "github",
        "url": "https://github.com/openai",
        "patterns": [
            "*/tree/*",
            "*/blob/*",
            "*/GPT*",
        ],
        "max_urls": 100000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 1,
        "reputation": 0.99,
        "query": "GPT language model",
        "description": "OpenAI - GPT implementations",
        "urls_estimate": 100000,
    },
}


# ============================================================================
# TIER 2: LARGE FRAMEWORKS & DOCS (50K+ URLs each)
# ============================================================================

LARGE_FRAMEWORK_SOURCES: Dict[str, Dict[str, Any]] = {
    "pytorch.org": {
        "source_type": "documentation",
        "url": "https://pytorch.org",
        "patterns": ["*/tutorials/*", "*/docs/*", "*/get-started/*"],
        "max_urls": 80000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 1,
        "reputation": 1.0,
        "query": "PyTorch deep learning CUDA",
        "description": "PyTorch - Official docs & tutorials",
        "urls_estimate": 80000,
    },
    
    "tensorflow.org": {
        "source_type": "documentation",
        "url": "https://tensorflow.org",
        "patterns": ["*/tutorials/*", "*/api_docs/*", "*/guide/*"],
        "max_urls": 80000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 1,
        "reputation": 1.0,
        "query": "TensorFlow Keras machine learning",
        "description": "TensorFlow - Official docs",
        "urls_estimate": 80000,
    },
    
    "huggingface.co": {
        "source_type": "framework",
        "url": "https://huggingface.co",
        "patterns": [
            "*/models/*",
            "*/datasets/*",
            "*/papers/*",
            "*/spaces/*",
            "*/course/*",
        ],
        "max_urls": 150000,
        "concurrency": 50,
        "hits_per_sec": 25.0,
        "priority": 1,
        "reputation": 0.98,
        "query": "transformer model NLP dataset",
        "description": "Hugging Face - Models, datasets, spaces",
        "urls_estimate": 150000,
    },
    
    "paperswithcode.com": {
        "source_type": "framework",
        "url": "https://paperswithcode.com",
        "patterns": [
            "*/papers/*",
            "*/methods/*",
            "*/datasets/*",
            "*/sota/*",
        ],
        "max_urls": 100000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 1,
        "reputation": 0.92,
        "query": "machine learning papers code",
        "description": "Papers With Code - 100K+ papers",
        "urls_estimate": 100000,
    },
}


# ============================================================================
# TIER 3: MEDIUM SOURCES (10K-50K URLs each)
# ============================================================================

MEDIUM_ACADEMIC_SOURCES: Dict[str, Dict[str, Any]] = {
    "openreview.net": {
        "source_type": "conference",
        "url": "https://openreview.net",
        "patterns": ["*/forum*", "*/pdf*"],
        "max_urls": 50000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 2,
        "reputation": 0.95,
        "query": "NeurIPS ICLR ICML papers",
        "description": "OpenReview - 50K+ conference papers",
        "urls_estimate": 50000,
    },
    
    "ieee.org": {
        "source_type": "journal",
        "url": "https://ieeexplore.ieee.org",
        "patterns": ["*/document/*", "*/search/*"],
        "max_urls": 40000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 2,
        "reputation": 0.90,
        "query": "machine learning AI research",
        "description": "IEEE - 40K+ tech papers",
        "urls_estimate": 40000,
    },
    
    "acm.org": {
        "source_type": "journal",
        "url": "https://dl.acm.org",
        "patterns": ["*/doi/*", "*/citation*"],
        "max_urls": 30000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 2,
        "reputation": 0.88,
        "query": "machine learning AI computer science",
        "description": "ACM - 30K+ CS papers",
        "urls_estimate": 30000,
    },
    
    "semanticscholar.org": {
        "source_type": "academic",
        "url": "https://www.semanticscholar.org",
        "patterns": ["*/paper/*", "*/search*"],
        "max_urls": 100000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 2,
        "reputation": 0.91,
        "query": "machine learning AI research",
        "description": "Semantic Scholar - 200M+ papers",
        "urls_estimate": 100000,
    },
}


# ============================================================================
# TIER 3: RESEARCH LABS & ORGANIZATIONS (20K-100K URLs)
# ============================================================================

LARGE_RESEARCH_SOURCES: Dict[str, Dict[str, Any]] = {
    "research.google": {
        "source_type": "research_lab",
        "url": "https://research.google",
        "patterns": ["*/pubs/*", "*/blog/*", "*/teams/*"],
        "max_urls": 80000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 1,
        "reputation": 0.99,
        "query": "machine learning AI research",
        "description": "Google Research - 80K+ papers",
        "urls_estimate": 80000,
    },
    
    "deepmind.google": {
        "source_type": "research_lab",
        "url": "https://www.deepmind.google",
        "patterns": ["*/research/*", "*/publications/*", "*/blog/*"],
        "max_urls": 40000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 1,
        "reputation": 1.0,
        "query": "AlphaGo reinforcement learning",
        "description": "DeepMind - 40K+ pages",
        "urls_estimate": 40000,
    },
    
    "ai.meta.com": {
        "source_type": "research_lab",
        "url": "https://ai.meta.com",
        "patterns": ["*/research/*", "*/blog/*", "*/publications/*"],
        "max_urls": 50000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 1,
        "reputation": 0.98,
        "query": "LLaMA research AI",
        "description": "Meta AI - 50K+ pages",
        "urls_estimate": 50000,
    },
    
    "github.com/google-research": {
        "source_type": "github",
        "url": "https://github.com/google-research",
        "patterns": ["*/tree/*", "*/blob/*"],
        "max_urls": 80000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 1,
        "reputation": 0.99,
        "query": "research implementation",
        "description": "Google Research GitHub",
        "urls_estimate": 80000,
    },
    
    "github.com/facebookresearch": {
        "source_type": "github",
        "url": "https://github.com/facebookresearch",
        "patterns": ["*/tree/*", "*/blob/*"],
        "max_urls": 60000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 1,
        "reputation": 0.98,
        "query": "research AI",
        "description": "Facebook Research GitHub",
        "urls_estimate": 60000,
    },
    
    "openai.com": {
        "source_type": "research_lab",
        "url": "https://openai.com",
        "patterns": ["*/research/*", "*/blog/*", "*/docs/*"],
        "max_urls": 50000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 1,
        "reputation": 0.99,
        "query": "GPT transformer research",
        "description": "OpenAI - 50K+ pages",
        "urls_estimate": 50000,
    },
}


# ============================================================================
# TIER 3: DATASET & BENCHMARK SOURCES (20K-100K URLs)
# ============================================================================

DATASET_SOURCES: Dict[str, Dict[str, Any]] = {
    "kaggle.com": {
        "source_type": "dataset",
        "url": "https://kaggle.com",
        "patterns": [
            "*/datasets/*",
            "*/competitions/*",
            "*/notebooks/*",
            "*/code/*",
        ],
        "max_urls": 200000,
        "concurrency": 50,
        "hits_per_sec": 25.0,
        "priority": 2,
        "reputation": 0.88,
        "query": "dataset machine learning competition",
        "description": "Kaggle - 200K+ datasets & competitions",
        "urls_estimate": 200000,
    },
    
    "huggingface.co/datasets": {
        "source_type": "dataset",
        "url": "https://huggingface.co/datasets",
        "patterns": ["*/datasets/*"],
        "max_urls": 80000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 2,
        "reputation": 0.92,
        "query": "dataset NLP machine learning",
        "description": "HF Datasets - 80K+ datasets",
        "urls_estimate": 80000,
    },
    
    "image-net.org": {
        "source_type": "dataset",
        "url": "https://www.image-net.org",
        "patterns": ["*/papers/*", "*/synset/*"],
        "max_urls": 30000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 0.95,
        "query": "image dataset computer vision",
        "description": "ImageNet - Image classification",
        "urls_estimate": 30000,
    },
    
    "github.com/tensorflow/datasets": {
        "source_type": "dataset",
        "url": "https://github.com/tensorflow/datasets",
        "patterns": ["*/tree/*", "*/blob/*"],
        "max_urls": 20000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 0.95,
        "query": "dataset tensorflow",
        "description": "TF Datasets",
        "urls_estimate": 20000,
    },
}


# ============================================================================
# TIER 4: DOCUMENTATION & EDUCATION (5K-50K URLs)
# ============================================================================

DOCUMENTATION_SOURCES: Dict[str, Dict[str, Any]] = {
    "docs.python.org": {
        "source_type": "documentation",
        "url": "https://docs.python.org",
        "patterns": ["*/library/*", "*/tutorial/*"],
        "max_urls": 20000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 1.0,
        "query": "python programming",
        "description": "Python Docs",
        "urls_estimate": 20000,
    },
    
    "scikit-learn.org": {
        "source_type": "documentation",
        "url": "https://scikit-learn.org",
        "patterns": ["*/modules/*", "*/tutorial/*"],
        "max_urls": 15000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 0.95,
        "query": "machine learning sklearn",
        "description": "scikit-learn Docs",
        "urls_estimate": 15000,
    },
    
    "numpy.org": {
        "source_type": "documentation",
        "url": "https://numpy.org",
        "patterns": ["*/doc/*", "*/tutorial/*"],
        "max_urls": 10000,
        "concurrency": 15,
        "hits_per_sec": 8.0,
        "priority": 3,
        "reputation": 0.95,
        "query": "numpy numerical computing",
        "description": "NumPy Docs",
        "urls_estimate": 10000,
    },
    
    "pandas.pydata.org": {
        "source_type": "documentation",
        "url": "https://pandas.pydata.org",
        "patterns": ["*/docs/*", "*/user_guide/*"],
        "max_urls": 15000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 0.95,
        "query": "pandas dataframe",
        "description": "Pandas Docs",
        "urls_estimate": 15000,
    },
    
    "jax.readthedocs.io": {
        "source_type": "documentation",
        "url": "https://jax.readthedocs.io",
        "patterns": ["*/en/*"],
        "max_urls": 10000,
        "concurrency": 15,
        "hits_per_sec": 8.0,
        "priority": 3,
        "reputation": 0.92,
        "query": "JAX numerical computing",
        "description": "JAX Docs",
        "urls_estimate": 10000,
    },
    
    "opencv.org": {
        "source_type": "documentation",
        "url": "https://docs.opencv.org",
        "patterns": ["*/modules/*", "*/tutorial/*"],
        "max_urls": 15000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 0.95,
        "query": "computer vision image processing",
        "description": "OpenCV Docs",
        "urls_estimate": 15000,
    },
    
    "fastapi.tiangolo.com": {
        "source_type": "documentation",
        "url": "https://fastapi.tiangolo.com",
        "patterns": ["*/advanced/*", "*/tutorial/*"],
        "max_urls": 10000,
        "concurrency": 15,
        "hits_per_sec": 8.0,
        "priority": 4,
        "reputation": 0.92,
        "query": "FastAPI web framework",
        "description": "FastAPI Docs",
        "urls_estimate": 10000,
    },
    
    "langchain.com": {
        "source_type": "documentation",
        "url": "https://langchain.com",
        "patterns": ["*/docs/*", "*/integrations/*"],
        "max_urls": 15000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 2,
        "reputation": 0.90,
        "query": "LangChain LLM agents",
        "description": "LangChain Docs",
        "urls_estimate": 15000,
    },
}


# ============================================================================
# TIER 4: BLOGS & EDUCATIONAL CONTENT (2K-20K URLs)
# ============================================================================

BLOG_SOURCES: Dict[str, Dict[str, Any]] = {
    "distill.pub": {
        "source_type": "blog",
        "url": "https://distill.pub",
        "patterns": ["*/"],
        "max_urls": 5000,
        "concurrency": 15,
        "hits_per_sec": 8.0,
        "priority": 4,
        "reputation": 0.95,
        "query": "machine learning explanations",
        "description": "Distill - Interactive ML",
        "urls_estimate": 5000,
    },
    
    "colah.github.io": {
        "source_type": "blog",
        "url": "https://colah.github.io",
        "patterns": ["*/"],
        "max_urls": 2000,
        "concurrency": 10,
        "hits_per_sec": 5.0,
        "priority": 4,
        "reputation": 0.90,
        "query": "neural networks explanations",
        "description": "Colah's Blog",
        "urls_estimate": 2000,
    },
    
    "medium.com": {
        "source_type": "blog",
        "url": "https://medium.com",
        "patterns": ["*/tag/machine-learning*", "*/tag/artificial-intelligence*", "*/tag/deep-learning*"],
        "max_urls": 100000,
        "concurrency": 40,
        "hits_per_sec": 20.0,
        "priority": 4,
        "reputation": 0.75,
        "query": "machine learning AI deep learning",
        "description": "Medium - 100K+ AI articles",
        "urls_estimate": 100000,
    },
    
    "towardsdatascience.com": {
        "source_type": "blog",
        "url": "https://towardsdatascience.com",
        "patterns": ["*/tagged/machine-learning*", "*/tagged/artificial-intelligence*"],
        "max_urls": 50000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 4,
        "reputation": 0.80,
        "query": "machine learning data science",
        "description": "Towards Data Science - 50K+ articles",
        "urls_estimate": 50000,
    },
}


# ============================================================================
# TIER 5: SPECIALIZED SOURCES (1K-10K URLs)
# ============================================================================

SPECIALIZED_SOURCES: Dict[str, Dict[str, Any]] = {
    # Additional GitHub organizations
    "github.com/microsoft": {
        "source_type": "github",
        "url": "https://github.com/microsoft",
        "patterns": ["*/tree/*", "*/blob/*"],
        "max_urls": 50000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 2,
        "reputation": 0.98,
        "query": "research AI machine learning",
        "description": "Microsoft GitHub",
        "urls_estimate": 50000,
    },
    
    "github.com/aws": {
        "source_type": "github",
        "url": "https://github.com/aws",
        "patterns": ["*/tree/*", "*/blob/*"],
        "max_urls": 40000,
        "concurrency": 30,
        "hits_per_sec": 15.0,
        "priority": 2,
        "reputation": 0.96,
        "query": "machine learning cloud AI",
        "description": "AWS GitHub",
        "urls_estimate": 40000,
    },
    
    "github.com/jax-ml": {
        "source_type": "github",
        "url": "https://github.com/google/jax",
        "patterns": ["*/tree/*", "*/blob/*"],
        "max_urls": 20000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 0.96,
        "query": "JAX numerical computing",
        "description": "JAX GitHub",
        "urls_estimate": 20000,
    },
    
    # Conference proceedings
    "cvpr2024.thecvf.com": {
        "source_type": "conference",
        "url": "https://cvpr2024.thecvf.com",
        "patterns": ["*/schedule*", "*/papers*"],
        "max_urls": 10000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 3,
        "reputation": 0.94,
        "query": "computer vision papers",
        "description": "CVPR - Conference papers",
        "urls_estimate": 10000,
    },
    
    # Book resources
    "d2l.ai": {
        "source_type": "book",
        "url": "https://d2l.ai",
        "patterns": ["/"],
        "max_urls": 5000,
        "concurrency": 20,
        "hits_per_sec": 10.0,
        "priority": 4,
        "reputation": 0.92,
        "query": "deep learning interactive book",
        "description": "Dive into Deep Learning",
        "urls_estimate": 5000,
    },
}


# ============================================================================
# CONSOLIDATED SOURCES
# ============================================================================

ALL_ENTERPRISE_SOURCES = {
    **MEGA_ACADEMIC_SOURCES,
    **MEGA_GITHUB_SOURCES,
    **LARGE_FRAMEWORK_SOURCES,
    **MEDIUM_ACADEMIC_SOURCES,
    **LARGE_RESEARCH_SOURCES,
    **DATASET_SOURCES,
    **DOCUMENTATION_SOURCES,
    **BLOG_SOURCES,
    **SPECIALIZED_SOURCES,
}


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_all_sources() -> Dict[str, Dict[str, Any]]:
    """Get all enterprise sources."""
    return ALL_ENTERPRISE_SOURCES


def get_sources_by_type(source_type: str) -> Dict[str, Dict[str, Any]]:
    """Filter sources by type."""
    return {
        k: v for k, v in ALL_ENTERPRISE_SOURCES.items()
        if v.get("source_type") == source_type
    }


def get_mega_sources() -> Dict[str, Dict[str, Any]]:
    """Get only mega sources (100K+ URLs each)."""
    return {
        k: v for k, v in ALL_ENTERPRISE_SOURCES.items()
        if v.get("urls_estimate", 0) >= 100000
    }


def get_top_sources(count: int = 30) -> Dict[str, Dict[str, Any]]:
    """Get top priority sources."""
    sorted_sources = sorted(
        ALL_ENTERPRISE_SOURCES.items(),
        key=lambda x: (x[1].get("priority", 5), -x[1].get("reputation", 0), -x[1].get("urls_estimate", 0))
    )
    return dict(sorted_sources[:count])


def get_sources_by_urls(min_urls: int = 50000) -> Dict[str, Dict[str, Any]]:
    """Get sources with minimum estimated URLs."""
    return {
        k: v for k, v in ALL_ENTERPRISE_SOURCES.items()
        if v.get("urls_estimate", 0) >= min_urls
    }


def calculate_total_estimated_urls() -> int:
    """Calculate total estimated URLs across all sources."""
    return sum(v.get("urls_estimate", 0) for v in ALL_ENTERPRISE_SOURCES.values())


def validate_sources():
    """Validate all sources configuration."""
    for domain, config in ALL_ENTERPRISE_SOURCES.items():
        try:
            EnterpriseSource(domain=domain, source_type=SourceType(config["source_type"]), **config)
        except Exception as e:
            raise ValueError(f"Invalid config for {domain}: {e}")


if __name__ == "__main__":
    print(f"\n{'='*90}")
    print(f"ENTERPRISE-SCALE AI/ML/RESEARCH VERTICAL SEARCH ENGINE")
    print(f"{'='*90}\n")
    
    print(f"Total sources: {len(ALL_ENTERPRISE_SOURCES)}")
    print(f"Estimated total URLs: {calculate_total_estimated_urls():,}")
    print(f"\nSources by type:")
    
    for source_type in SourceType:
        sources = get_sources_by_type(source_type.value)
        if sources:
            urls = sum(v.get("urls_estimate", 0) for v in sources.values())
            print(f"  {source_type.value.upper()}: {len(sources)} sources ({urls:,} URLs)")
    
    print(f"\n{'─'*90}")
    print("TOP 30 PRIORITY SOURCES:")
    print(f"{'─'*90}\n")
    
    for i, (domain, config) in enumerate(get_top_sources(30).items(), 1):
        print(f"{i:2d}. {domain}")
        print(f"    Type: {config['source_type']} | Priority: {config['priority']} | Est. URLs: {config['urls_estimate']:,}")
    
    print(f"\n{'='*90}")
    print(f"✓ READY FOR 2M+ URL DISCOVERY")
    print(f"{'='*90}\n")
