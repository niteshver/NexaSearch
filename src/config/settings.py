from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings, DotEnvSettingsSource, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "NexaSearch"
    DEBUG: bool = True

    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parents[2]
    DUCKDB_PATH: str = "data/nexasearch.db"
    INDEX_DIR: str = "data/index"

    # Crawling Settings
    CRAWL_MAX_DEPTH: int = 2
    CRAWL_MAX_PAGES: int = 50
    CRAWL_CONCURRENT: int = 5
    CRAWL_TIMEOUT: int = 30
    CRAWL_USER_AGENT: str = "NexaSearchCrawler/0.1.0"
    CRAWL_KEYWORDS: str = "AI,LLM,agent,machine learning,deep learning,neural network,python,pypi,research paper,arxiv,github"
    PRUNING_THRESHOLD: float = 0.6
    WAIT_UNTIL: str = "load"
    MAX_RETRIES: int = 3
    WORD_COUNT_THRESHOLD: int = 10
    LOG_LEVEL: str = "INFO"

    # Quality Filtering Settings
    QUALITY_THRESHOLD: float = 0.6
    MIN_WORD_COUNT: int = 50
    MAX_WORD_COUNT: int = 10000
    USE_DISTILBERT_CLASSIFIER: bool = False

    # Deduplication Settings
    JACCARD_THRESHOLD: float = 0.85
    NUM_PERMUTATIONS: int = 128

    # Chunking Settings
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 100

    # Models
    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    CROSS_ENCODER_MODEL_NAME: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    # Weights
    BM25_WEIGHT: float = 0.5
    VECTOR_WEIGHT: float = 0.5
    QUALITY_WEIGHT: float = 0.2

    # APIs (Optional)
    GITHUB_TOKEN: str = ""
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_prefix="NEXASEARCH_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        # Keep the existing unprefixed .env file working while isolating
        # runtime configuration from unrelated shell variables such as DEBUG.
        legacy_dotenv_settings = DotEnvSettingsSource(
            settings_cls,
            env_file=".env",
            env_file_encoding="utf-8",
            env_prefix="",
        )
        return (
            init_settings,
            env_settings,
            legacy_dotenv_settings,
            file_secret_settings,
        )

    @property
    def keywords_list(self) -> List[str]:
        return [k.strip().lower() for k in self.CRAWL_KEYWORDS.split(",") if k.strip()]

    @property
    def absolute_db_path(self) -> Path:
        path = Path(self.DUCKDB_PATH)
        if path.is_absolute():
            return path
        return self.BASE_DIR / path

    @property
    def absolute_index_dir(self) -> Path:
        path = Path(self.INDEX_DIR)
        if path.is_absolute():
            return path
        return self.BASE_DIR / path

settings = Settings()
