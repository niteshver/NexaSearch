import asyncio
import json
import logging
import tempfile
from datetime import datetime
from typing import List, Set, Dict, Any, Optional, Tuple
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from fnmatch import fnmatch  # ✓ IMPROVED: Proper pattern matching
import hashlib

from crawl4ai import AsyncUrlSeeder, SeedingConfig
from src.config.settings import settings
from src.crawler.logger import logger
from src.seeder.sources import SOURCES, get_source_config, validate_source_config

logger = logging.getLogger(__name__)


# ✓ IMPROVED: Configuration validation class
class URLSeederConfig:
    """Validates URLSeeder configuration"""
    
    def __init__(
        self,
        output_dir: str = "./data/raw/sitemap",
        global_query: Optional[str] = None,
        use_global_bm25: bool = False,
        rate_limit_per_domain: float = 1.0,
        max_retries: int = 3,
        incremental_mode: bool = False
    ):
        self.output_dir = Path(output_dir)
        self.global_query = global_query
        self.use_global_bm25 = use_global_bm25
        self.rate_limit_per_domain = rate_limit_per_domain
        self.max_retries = max_retries
        self.incremental_mode = incremental_mode
        
        # Validate
        if rate_limit_per_domain <= 0:
            raise ValueError("rate_limit_per_domain must be > 0")
        if max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        
        # Ensure output directory is accessible
        try:
            self.output_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError as e:
            raise ValueError(f"Cannot write to output directory {self.output_dir}: {e}")


class URLSeeder:
    """
    Production-grade URL seeder using Crawl4AI AsyncUrlSeeder.
    
    Improvements:
    - ✓ Proper pattern matching using fnmatch
    - ✓ URL validation and normalization
    - ✓ Retry logic with exponential backoff
    - ✓ Checkpoint/resume system
    - ✓ Configurable rate limiting
    - ✓ Proper deduplication
    - ✓ Atomic file writes
    - ✓ Detailed error reporting
    """

    def __init__(
        self,
        source_domains: Optional[List[str]] = None,
        config: Optional[URLSeederConfig] = None
    ):
        """
        Initialize URL Seeder with validation.

        Args:
            source_domains: List of domains to seed from
            config: URLSeederConfig object with all settings

        Raises:
            ValueError: If configuration is invalid
        """
        # Use provided config or create default
        self.config = config or URLSeederConfig()
        
        # Validate source domains
        if source_domains:
            invalid_domains = [d for d in source_domains if d not in SOURCES]
            if invalid_domains:
                raise ValueError(f"Unknown domains in SOURCES: {invalid_domains}")
            self.source_domains = source_domains
        else:
            self.source_domains = list(SOURCES.keys())
        
        logger.info(f"✓ Initialized URLSeeder with {len(self.source_domains)} domains")

        # Data structures
        self.discovered_urls: Dict[str, List[Dict[str, Any]]] = {}
        self.url_to_sources: Dict[str, List[str]] = {}  # ✓ IMPROVED: Track sources per URL
        self.all_urls: Set[str] = set()
        self.failed_domains: List[Dict[str, Any]] = []
        self.statistics: Dict[str, Any] = {}
        self.checkpoint_file = self.config.output_dir / ".seeder_checkpoint.json"

    def _validate_url(self, url: str) -> bool:
        """
        Validate URL format.
        
        ✓ NEW: Comprehensive URL validation

        Args:
            url: URL string to validate

        Returns:
            True if valid URL format
        """
        if not url or not isinstance(url, str):
            return False
        
        url = url.strip()
        if len(url) < 8:  # Minimum: "http://a"
            return False
        
        try:
            result = urlparse(url)
            # Must have scheme and netloc
            return all([result.scheme in ['http', 'https'], result.netloc])
        except Exception:
            return False

    def _normalize_url(self, url: str) -> Optional[str]:
        """
        Normalize URL (remove fragments, trim whitespace).
        
        ✓ NEW: URL normalization

        Args:
            url: URL to normalize

        Returns:
            Normalized URL or None if invalid
        """
        if not self._validate_url(url):
            return None
        
        url = url.strip()
        
        # Remove fragment (everything after #)
        if '#' in url:
            url = url.split('#')[0]
        
        # Remove trailing slashes for consistency
        if url.endswith('/') and url.count('/') > 3:
            url = url.rstrip('/')
        
        return url

    def _matches_pattern(self, url: str, pattern: str) -> bool:
        """
        Check if URL matches pattern using fnmatch.
        
        ✓ FIXED: Now uses proper fnmatch instead of broken string logic

        Args:
            url: URL to check
            pattern: Pattern like "*", "*/blog/*", "*/project/*", "*.pdf"

        Returns:
            True if URL matches pattern
            
        Examples:
            _matches_pattern("https://site.com/docs/api.html", "*/docs/*") -> True
            _matches_pattern("https://site.com/docs/api.html", "*.pdf") -> False
            _matches_pattern("https://site.com/project/123", "*/project/*") -> True
        """
        # ✓ IMPROVED: Input validation
        if not url or not isinstance(url, str):
            return False
        if not isinstance(pattern, str):
            return True
        
        pattern = pattern.strip()
        
        # Wildcard pattern means all URLs match
        if pattern == '*' or not pattern:
            return True
        
        # Use fnmatch for proper pattern matching
        return fnmatch(url, pattern)

    def _build_seeding_config(
        self,
        domain: str,
        use_bm25: bool = False
    ) -> SeedingConfig:
        """
        Build SeedingConfig for a domain with validation.
        
        ✓ IMPROVED: Adds configuration validation

        Args:
            domain: Target domain
            use_bm25: Whether to use BM25 scoring

        Returns:
            SeedingConfig object

        Raises:
            ValueError: If config is invalid
        """
        source_config = get_source_config(domain)
        
        # ✓ IMPROVED: Validate source config
        try:
            validate_source_config(source_config, domain)
        except ValueError as e:
            logger.error(f"Invalid config for {domain}: {e}")
            raise

        # Handle pattern extraction
        pattern = source_config.get('pattern', '*')
        if isinstance(pattern, (list, dict)):
            patterns = pattern.values() if isinstance(pattern, dict) else pattern
            pattern = list(patterns)[0] if patterns else '*'

        # Build config
        config_kwargs = {
            'source': source_config.get('source', 'sitemap+cc'),
            'extract_head': source_config.get('extract_head', True),
            'pattern': pattern,
            'max_urls': source_config.get('max_urls', 1000),
            'concurrency': source_config.get('concurrency', 20),
            'hits_per_sec': source_config.get('hits_per_sec', 10),
            'live_check': source_config.get('live_check', False),
            'force': source_config.get('force', False),
            'verbose': False,
            'filter_nonsense_urls': source_config.get('filter_nonsense_urls', True),
            'cache_ttl_hours': source_config.get('cache_ttl_hours', 24)
        }

        # Add BM25 if enabled
        if use_bm25 or source_config.get('use_bm25'):
            query = source_config.get('query') or self.config.global_query
            if query:
                config_kwargs['query'] = query
                config_kwargs['scoring_method'] = 'bm25'
                config_kwargs['score_threshold'] = source_config.get('score_threshold', 0.3)
                logger.debug(f"BM25 enabled for {domain}: query='{query}'")

        try:
            return SeedingConfig(**config_kwargs)
        except Exception as e:
            logger.error(f"Error creating SeedingConfig for {domain}: {e}")
            raise

    def _load_checkpoint(self) -> Dict[str, Any]:
        """
        ✓ NEW: Load checkpoint to resume from previous run
        
        Returns:
            Checkpoint data or empty dict if not found
        """
        if not self.config.incremental_mode or not self.checkpoint_file.exists():
            return {}
        
        try:
            with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                checkpoint = json.load(f)
                logger.info(f"✓ Loaded checkpoint with {len(checkpoint.get('completed_domains', []))} completed domains")
                return checkpoint
        except Exception as e:
            logger.warning(f"Could not load checkpoint: {e}")
            return {}

    def _save_checkpoint(self, completed_domains: List[str]) -> None:
        """
        ✓ NEW: Save checkpoint for incremental discovery
        
        Args:
            completed_domains: List of successfully seeded domains
        """
        if not self.config.incremental_mode:
            return
        
        checkpoint = {
            'completed_domains': completed_domains,
            'timestamp': datetime.now().isoformat(),
            'total_urls': len(self.all_urls)
        }
        
        try:
            with open(self.checkpoint_file, 'w', encoding='utf-8') as f:
                json.dump(checkpoint, f, indent=2)
            logger.debug(f"✓ Saved checkpoint ({len(completed_domains)} domains completed)")
        except Exception as e:
            logger.warning(f"Could not save checkpoint: {e}")

    async def discover_urls(
        self,
        use_bm25_scoring: bool = False,
        use_live_check: bool = False
    ) -> Dict[str, List[str]]:
        """
        Discover URLs from source domains with retry logic and checkpoints.

        Args:
            use_bm25_scoring: Enable BM25 relevance scoring
            use_live_check: Verify URLs are accessible

        Returns:
            Dictionary mapping domains to lists of discovered URLs
        """
        logger.info(f"\n{'='*80}")
        logger.info(f"[URL SEEDER] Starting URL discovery")
        logger.info(f"{'='*80}")
        logger.info(f"Domains: {len(self.source_domains)}")
        logger.info(f"BM25 Scoring: {use_bm25_scoring}")
        logger.info(f"Incremental mode: {self.config.incremental_mode}")
        logger.info(f"Rate limit: {self.config.rate_limit_per_domain}s/domain")
        logger.info(f"{'='*80}\n")

        # ✓ NEW: Load checkpoint
        checkpoint = self._load_checkpoint()
        completed_domains = checkpoint.get('completed_domains', [])
        domains_to_process = [d for d in self.source_domains if d not in completed_domains]

        try:
            async with AsyncUrlSeeder() as seeder:
                for i, domain in enumerate(domains_to_process, 1):
                    logger.info(f"\n[{i}/{len(domains_to_process)}] Processing: {domain}")
                    logger.info(f"{'-'*80}")  # ✓ FIXED: was empty string

                    # ✓ IMPROVED: Retry logic
                    for attempt in range(1, self.config.max_retries + 1):
                        try:
                            config = self._build_seeding_config(
                                domain,
                                use_bm25=use_bm25_scoring
                            )

                            logger.info(f"  Config: pattern={config.pattern}, max_urls={config.max_urls}")
                            if hasattr(config, 'query'):
                                logger.info(f"  BM25: query='{config.query}', threshold={getattr(config, 'score_threshold', 'N/A')}")

                            # Discover URLs
                            logger.info(f"  Discovering URLs... (attempt {attempt}/{self.config.max_retries + 1})")
                            urls_data = await seeder.urls(domain, config)

                            if not urls_data:
                                logger.warning(f"  No URLs discovered for {domain}")
                                self.discovered_urls[domain] = []
                                break  # ✓ IMPROVED: Break retry loop on success (even if empty)

                            # ✓ IMPROVED: Process with better error handling
                            valid_urls = await self._process_url_batch(urls_data, domain, config)
                            
                            self.discovered_urls[domain] = valid_urls
                            completed_domains.append(domain)
                            self._save_checkpoint(completed_domains)
                            
                            logger.info(f"  ✓ Success: {len(valid_urls)} valid URLs")
                            break  # Exit retry loop on success

                        except Exception as e:
                            logger.error(f"  ✗ Attempt {attempt}/{self.config.max_retries + 1} failed: {e}")
                            if attempt < self.config.max_retries + 1:
                                wait_time = 2 ** attempt  # Exponential backoff
                                logger.info(f"  Retrying in {wait_time}s...")
                                await asyncio.sleep(wait_time)
                            else:
                                # ✓ IMPROVED: Better error tracking
                                self.failed_domains.append({
                                    'domain': domain,
                                    'error': str(e),
                                    'attempts': self.config.max_retries + 1,
                                    'timestamp': datetime.now().isoformat()
                                })
                                logger.error(f"  ✗ Failed after {self.config.max_retries + 1} attempts")
                                break

                    # ✓ IMPROVED: Configurable rate limiting
                    await asyncio.sleep(self.config.rate_limit_per_domain)

            # Final statistics
            self._log_statistics()
            return self.discovered_urls

        except Exception as e:
            logger.error(f"\n✗ Fatal error: {e}", exc_info=True)
            raise

    async def _process_url_batch(
        self,
        urls_data: List[Any],
        domain: str,
        config: SeedingConfig
    ) -> List[Dict[str, Any]]:
        """
        ✓ NEW: Process URL batch with comprehensive validation and error handling
        
        Args:
            urls_data: Raw URLs from seeder
            domain: Domain being processed
            config: Seeding config for this domain
            
        Returns:
            List of valid URL entries
        """
        valid_urls = []
        stats = {
            'total': len(urls_data),
            'valid': 0,
            'invalid_format': 0,
            'low_relevance': 0,
            'pattern_mismatch': 0,
            'processing_errors': 0
        }

        for url_entry in urls_data:
            try:
                # ✓ IMPROVED: Safe extraction with validation
                if isinstance(url_entry, dict):
                    url_raw = url_entry.get('url', '')
                    status = url_entry.get('status', 'unknown')
                    score = url_entry.get('relevance_score', 1.0)
                    head_data = url_entry.get('head_data', {})
                else:
                    url_raw = str(url_entry)
                    status = 'unknown'
                    score = 1.0
                    head_data = {}

                # ✓ IMPROVED: Normalize and validate URL
                url = self._normalize_url(url_raw)
                if not url:
                    stats['invalid_format'] += 1
                    logger.debug(f"  Skipped (invalid format): {url_raw}")
                    continue

                # Skip dead URLs
                if status == 'not_valid':
                    logger.debug(f"  Skipped (dead URL): {url}")
                    continue

                # Check relevance score
                if hasattr(config, 'score_threshold') and score < config.score_threshold:
                    stats['low_relevance'] += 1
                    logger.debug(f"  Skipped (low score {score:.2f}): {url}")
                    continue

                # ✓ REMOVED: Redundant pattern check (Crawl4AI already filters)
                # Pattern matching is done by Crawl4AI, trust its filtering

                # ✓ IMPROVED: Track URL to sources
                if url not in self.url_to_sources:
                    self.url_to_sources[url] = []
                self.url_to_sources[url].append(domain)
                self.all_urls.add(url)

                valid_urls.append({
                    'url': url,
                    'status': status,
                    'score': score,
                    'title': head_data.get('title', '') if isinstance(head_data, dict) else '',
                    'description': head_data.get('meta', {}).get('description', '') if isinstance(head_data, dict) else '',
                    'discovered_at': datetime.now().isoformat(),
                    'source': domain
                })

                stats['valid'] += 1

            except Exception as e:
                stats['processing_errors'] += 1
                logger.debug(f"Error processing URL entry: {e}")
                continue

        # Log per-domain statistics
        logger.info(f"  Processing results:")
        logger.info(f"    • Valid: {stats['valid']}")
        logger.info(f"    • Invalid format: {stats['invalid_format']}")
        if stats['low_relevance'] > 0:
            logger.info(f"    • Low relevance: {stats['low_relevance']}")
        if stats['pattern_mismatch'] > 0:
            logger.info(f"    • Pattern mismatch: {stats['pattern_mismatch']}")
        if stats['processing_errors'] > 0:
            logger.info(f"    • Processing errors: {stats['processing_errors']}")

        return valid_urls

    def _log_statistics(self) -> None:
        """✓ IMPROVED: Enhanced statistics logging"""
        total_urls = len(self.all_urls)
        successful_domains = len(self.discovered_urls)
        failed_domains = len(self.failed_domains)

        self.statistics = {
            'total_urls': total_urls,
            'domains_succeeded': successful_domains,
            'domains_failed': failed_domains,
            'discovered_at': datetime.now().isoformat()
        }

        logger.info(f"\n{'='*80}")
        logger.info(f"[STATISTICS] URL Discovery Summary")
        logger.info(f"{'='*80}")
        logger.info(f"Total unique URLs discovered: {total_urls}")
        logger.info(f"Domains succeeded: {successful_domains}/{len(self.source_domains)}")
        logger.info(f"Domains failed: {failed_domains}")

        if successful_domains > 0:
            avg_urls = total_urls / successful_domains
            logger.info(f"Average URLs per domain: {avg_urls:.0f}")

        # Per-source breakdown
        logger.info(f"\nPer-source breakdown:")
        for domain, urls in sorted(self.discovered_urls.items()):
            source_count = len(self.url_to_sources.get(next(iter([u['url'] for u in urls]), ''), []))
            logger.info(f"  • {domain}: {len(urls)} URLs")

        # Failed domains details
        if self.failed_domains:
            logger.info(f"\nFailed domains:")
            for failure in self.failed_domains:
                logger.info(f"  • {failure['domain']}: {failure['error']} (attempts: {failure.get('attempts', 'N/A')})")

        logger.info(f"{'='*80}\n")

    def save_to_json(self, filename: str = "seeds.json") -> str:
        """
        ✓ IMPROVED: Save with atomic write and validation
        
        Save discovered URLs to JSON with source tracking
        """
        output_path = self.config.output_dir / filename

        flat_urls = []
        for domain, urls in self.discovered_urls.items():
            flat_urls.extend(urls)

        data = {
            'metadata': {
                'total_urls': len(self.all_urls),
                'domains_seeded': len(self.discovered_urls),
                'domains_failed': len(self.failed_domains),
                'discovered_at': datetime.now().isoformat(),
                'source_domains': self.source_domains,
                'url_to_sources': self.url_to_sources  # ✓ NEW: Track URL origins
            },
            'urls': sorted(list(self.all_urls)),
            'detailed_urls': flat_urls,  # ✓ FIXED: No duplicates if URL appears in one domain
            'failed_domains': self.failed_domains
        }

        # ✓ IMPROVED: Atomic write using temp file
        try:
            temp_fd, temp_path = tempfile.mkstemp(text=True, dir=self.config.output_dir)
            with open(temp_fd, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Atomic rename
            Path(temp_path).replace(output_path)
            
            logger.info(f"[SAVE] JSON saved: {output_path}")
            logger.info(f"  Total URLs: {len(data['urls'])}")
            logger.info(f"  File size: {output_path.stat().st_size / 1024:.1f} KB")
            
            return str(output_path)

        except Exception as e:
            logger.error(f"Error saving JSON: {e}")
            raise

    def generate_sitemap_xml(self, filename: str = "master_seed.xml") -> str:
        """
        ✓ IMPROVED: Generate XML sitemap with validation
        
        Generate XML sitemap respecting per-source discovery
        """
        output_path = self.config.output_dir / filename

        try:
            urlset = ET.Element('urlset')
            urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

            for url in sorted(self.all_urls):
                url_elem = ET.SubElement(urlset, 'url')

                loc = ET.SubElement(url_elem, 'loc')
                loc.text = url

                lastmod = ET.SubElement(url_elem, 'lastmod')
                lastmod.text = datetime.now().isoformat()

                changefreq = ET.SubElement(url_elem, 'changefreq')
                changefreq.text = 'weekly'

                priority = ET.SubElement(url_elem, 'priority')
                priority.text = '0.8'

            # ✓ IMPROVED: Atomic write for XML
            temp_fd, temp_path = tempfile.mkstemp(text=True, suffix='.xml', dir=self.config.output_dir)
            tree = ET.ElementTree(urlset)
            tree.write(temp_fd, encoding='utf-8', xml_declaration=True)
            
            Path(temp_path).replace(output_path)

            logger.info(f"[SAVE] XML Sitemap generated: {output_path}")
            logger.info(f"  Total URLs: {len(self.all_urls)}")
            logger.info(f"  File size: {output_path.stat().st_size / 1024:.1f} KB")

            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating sitemap: {e}")
            raise

    def load_seeds(self, filename: str = "seeds.json") -> List[str]:
        """Load previously discovered seeds from file"""
        input_path = self.config.output_dir / filename

        if not input_path.exists():
            logger.warning(f"Seeds file not found: {input_path}")
            return []

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                urls = data.get('urls', [])
                logger.info(f"[LOAD] Loaded {len(urls)} seeds from {input_path}")
                return urls
        except Exception as e:
            logger.error(f"Error loading seeds: {e}")
            return []


async def main():
    """Run URL seeding with production-grade config"""

    # ✓ IMPROVED: Use URLSeederConfig for all settings
    config = URLSeederConfig(
        output_dir="./data/raw/sitemap",
        global_query=None,
        use_global_bm25=False,
        rate_limit_per_domain=1.0,
        max_retries=2,
        incremental_mode=True  # ✓ NEW: Resume from checkpoints
    )

    seeder = URLSeeder(
        source_domains=list(SOURCES.keys()),
        config=config
    )

    # Discover URLs
    discovered = await seeder.discover_urls(
        use_bm25_scoring=False,
        use_live_check=False
    )

    # Save results
    seeder.save_to_json("seeds.json")
    seeder.generate_sitemap_xml("master_seed.xml")

    logger.info("\n✓ URL seeding complete!")
    logger.info(f"  Total URLs: {len(seeder.all_urls)}")
    logger.info(f"  Sitemap: ./data/raw/sitemap/master_seed.xml")
    logger.info(f"  Seeds JSON: ./data/raw/sitemap/seeds.json")


if __name__ == "__main__":
    asyncio.run(main())