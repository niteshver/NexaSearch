import asyncio
import json
import logging
from datetime import datetime
from typing import List, Set, Dict, Any, Optional
from pathlib import Path
import xml.etree.ElementTree as ET

from crawl4ai import AsyncUrlSeeder, SeedingConfig
from src.config.settings import settings
from src.crawler.logger import logger
from src.seeder.sources import SOURCES, get_source_config

logger = logging.getLogger(__name__)


class URLSeeder:
    """
    Production-grade URL seeder using Crawl4AI AsyncUrlSeeder.
    - Honors per-source seeding configurations
    - Respects source-specific patterns and filters
    - Discovers URLs from sitemap + Common Crawl
    - Generates master_seed.xml sitemap
    """

    def __init__(
        self,
        source_domains: Optional[List[str]] = None,
        output_dir: str = "./data/raw/sitemap",
        global_query: Optional[str] = None,
        use_global_bm25: bool = False
    ):
        """
        Initialize URL Seeder with support for per-source configs.

        Args:
            source_domains: List of domains to seed from
            output_dir: Directory to save sitemap and seeds
            global_query: Optional global BM25 query (can be overridden per-source)
            use_global_bm25: Whether to apply global BM25 scoring
        """
        self.source_domains = source_domains or list(SOURCES.keys())  # FIXED: Use .keys()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.global_query = global_query
        self.use_global_bm25 = use_global_bm25

        self.discovered_urls: Dict[str, List[Dict[str, Any]]] = {}
        self.all_urls: Set[str] = set()
        self.failed_domains: List[Dict[str, str]] = []
        self.statistics: Dict[str, Any] = {}

    def _build_seeding_config(
        self,
        domain: str,
        global_query: Optional[str] = None,
        use_bm25: bool = False
    ) -> SeedingConfig:
        """
        Build SeedingConfig for a domain, respecting per-source configurations.

        Priority:
        1. Per-source config from sources.py
        2. Global config with fallback defaults

        Args:
            domain: Target domain
            global_query: Optional global BM25 query
            use_bm25: Whether to use BM25 scoring

        Returns:
            SeedingConfig object
        """
        # Get per-source configuration
        source_config = get_source_config(domain)

        # Get pattern - handle both single pattern and multiple patterns
        pattern = source_config.get('pattern', '*')
        if isinstance(pattern, list) and pattern:
            # FIXED: Handle list of patterns
            pattern = pattern[0]  # Use first pattern if multiple
        elif isinstance(pattern, dict):
            # FIXED: Handle patterns dictionary (e.g., GitHub)
            patterns = list(pattern.values())
            pattern = patterns[0] if patterns else '*'

        # Build config with per-source values
        config_kwargs = {
            'source': source_config.get('source', 'sitemap+cc'),
            'extract_head': source_config.get('extract_head', True),
            'pattern': pattern,  # Per-source pattern!
            'max_urls': source_config.get('max_urls', 1000),
            'concurrency': source_config.get('concurrency', 20),
            'hits_per_sec': source_config.get('hits_per_sec', 10),
            'live_check': source_config.get('live_check', False),
            'force': source_config.get('force', False),
            'verbose': False,
            'filter_nonsense_urls': source_config.get('filter_nonsense_urls', True),
            'cache_ttl_hours': source_config.get('cache_ttl_hours', 24)
        }

        # Add BM25 scoring if enabled
        if use_bm25 or source_config.get('use_bm25'):
            # Per-source query takes precedence
            query = source_config.get('query') or global_query
            score_threshold = source_config.get('score_threshold', 0.3)

            if query:
                config_kwargs['query'] = query
                config_kwargs['scoring_method'] = 'bm25'
                config_kwargs['score_threshold'] = score_threshold

        # FIXED: Add validation logging
        logger.debug(f"Built SeedingConfig for {domain}:")
        logger.debug(f"  Pattern: {config_kwargs['pattern']}")
        logger.debug(f"  Source: {config_kwargs['source']}")
        if 'query' in config_kwargs:
            logger.debug(f"  Query: {config_kwargs['query']}")
            logger.debug(f"  Score threshold: {config_kwargs['score_threshold']}")

        try:
            return SeedingConfig(**config_kwargs)
        except Exception as e:
            logger.error(f"Error creating SeedingConfig for {domain}: {e}")
            raise

    async def discover_urls(
        self,
        use_bm25_scoring: bool = False,
        use_live_check: bool = False
    ) -> Dict[str, List[str]]:
        """
        Discover URLs from source domains using per-source configurations.

        Args:
            use_bm25_scoring: Enable BM25 relevance scoring (per-source overrides)
            use_live_check: Verify URLs are accessible

        Returns:
            Dictionary mapping domains to lists of discovered URLs
        """
        logger.info(f"\n{'='*80}")
        logger.info(f"[URL SEEDER] Starting URL discovery from {len(self.source_domains)} domains")
        logger.info(f"{'='*80}")
        logger.info(f"Source domains: {', '.join(self.source_domains)}")
        logger.info(f"Respecting per-source configurations from sources.py")
        logger.info(f"Global BM25: {use_bm25_scoring}")
        logger.info(f"Global query: {self.global_query or 'None'}")
        logger.info(f"{'='*80}\n")

        try:
            async with AsyncUrlSeeder() as seeder:

                for i, domain in enumerate(self.source_domains, 1):
                    logger.info(f"\n[{i}/{len(self.source_domains)}] Seeding: {domain}")
                    logger.info(f"{''*80}")

                    try:
                        # Build per-source config
                        config = self._build_seeding_config(
                            domain,
                            global_query=self.global_query,
                            use_bm25=use_bm25_scoring
                        )

                        # Log what we're about to seed
                        source_cfg = get_source_config(domain)
                        logger.info(f"  Configuration:")
                        logger.info(f"    • Source: {config.source}")
                        logger.info(f"    • Pattern: {config.pattern}")

                        # FIXED: Safe attribute access with getattr
                        if hasattr(config, 'query') and getattr(config, 'query', None):
                            logger.info(f"    • Query: {config.query}")
                            logger.info(f"    • Score threshold: {getattr(config, 'score_threshold', 'N/A')}")

                        logger.info(f"    • Max URLs: {config.max_urls}")
                        logger.info(f"    • Live check: {config.live_check}")

                        # Discover URLs
                        logger.info(f"  Discovering URLs...")
                        urls_data = await seeder.urls(domain, config)

                        # FIXED: Handle empty results
                        if not urls_data:
                            logger.warning(f"  No URLs discovered for {domain}")
                            self.discovered_urls[domain] = []
                            await asyncio.sleep(1)
                            continue

                        # Process and filter results
                        valid_urls = []
                        live_count = 0
                        dead_count = 0
                        low_score_count = 0
                        pattern_mismatch_count = 0

                        for url_entry in urls_data:
                            try:
                                # FIXED: Safe dictionary access
                                url = url_entry.get('url') if isinstance(url_entry, dict) else str(url_entry)
                                status = url_entry.get('status', 'unknown') if isinstance(url_entry, dict) else 'unknown'
                                score = url_entry.get('relevance_score', 1.0) if isinstance(url_entry, dict) else 1.0
                                head_data = url_entry.get('head_data', {}) if isinstance(url_entry, dict) else {}

                                # Skip invalid URLs
                                if not url or status == 'not_valid':
                                    dead_count += 1
                                    continue

                                # Skip low-scoring URLs (if BM25 enabled)
                                if use_bm25_scoring and hasattr(config, 'score_threshold'):
                                    threshold = getattr(config, 'score_threshold', 0.3)
                                    if score < threshold:
                                        low_score_count += 1
                                        continue

                                # Verify pattern match (double-check source-specific filter)
                                if not self._matches_pattern(url, config.pattern):
                                    pattern_mismatch_count += 1
                                    logger.debug(f"  Skipped (pattern mismatch): {url}")
                                    continue

                                live_count += 1
                                valid_urls.append({
                                    'url': url,
                                    'status': status,
                                    'score': score,
                                    'title': head_data.get('title', '') if isinstance(head_data, dict) else '',
                                    'description': head_data.get('meta', {}).get('description', '') if isinstance(head_data, dict) else '',
                                    'discovered_at': datetime.now().isoformat(),
                                    'source': domain
                                })
                                self.all_urls.add(url)

                            except Exception as e:
                                logger.debug(f"Error processing URL entry: {e}")
                                continue

                        # Store results
                        self.discovered_urls[domain] = valid_urls

                        # Log statistics
                        logger.info(f"  ✓ Discovery complete:")
                        logger.info(f"    • Valid URLs: {live_count}")
                        logger.info(f"    • Dead URLs: {dead_count}")
                        if use_bm25_scoring:
                            logger.info(f"    • Low relevance (filtered): {low_score_count}")
                        if pattern_mismatch_count > 0:
                            logger.info(f"    • Pattern mismatch (filtered): {pattern_mismatch_count}")
                        logger.info(f"    • Unique URLs added: {len(valid_urls)}")

                        # Rate limiting between domains
                        await asyncio.sleep(1)

                    except Exception as e:
                        logger.error(f"  ✗ Error seeding {domain}: {str(e)}", exc_info=True)
                        self.failed_domains.append({
                            'domain': domain,
                            'error': str(e),
                            'timestamp': datetime.now().isoformat()
                        })
                        continue

            # Final statistics
            self._log_statistics()
            return self.discovered_urls

        except Exception as e:
            logger.error(f"\n✗ Fatal error in URL discovery: {str(e)}", exc_info=True)
            raise

    def _matches_pattern(self, url: str, pattern: str) -> bool:
        """
        Check if URL matches the pattern filter.
        Supports wildcard patterns like */blog/*, */project/*, etc.

        Args:
            url: URL to check
            pattern: Pattern like "*", "*/blog/*", "*.pdf"

        Returns:
            True if URL matches pattern
        """
        # FIXED: Add validation
        if not url or not isinstance(url, str):
            return False

        if not isinstance(pattern, str):
            return True

        if pattern == '*':
            return True

        # Convert pattern to regex-like matching
        clean_pattern = pattern.strip()
        if clean_pattern.startswith('*'):
            clean_pattern = clean_pattern.lstrip('*')
        if clean_pattern.endswith('*'):
            clean_pattern = clean_pattern.rstrip('*')

        return clean_pattern in url

    def _log_statistics(self):
        """Log discovery statistics"""
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
        logger.info(f"Domains successfully seeded: {successful_domains}/{len(self.source_domains)}")
        logger.info(f"Domains failed: {failed_domains}")

        if successful_domains > 0:
            avg_urls = total_urls / successful_domains
            logger.info(f"Average URLs per domain: {avg_urls:.0f}")

        # Per-source breakdown
        logger.info(f"\nPer-source breakdown:")
        for domain, urls in sorted(self.discovered_urls.items()):
            logger.info(f"  • {domain}: {len(urls)} URLs")

        logger.info(f"{'='*80}\n")

    def save_to_json(self, filename: str = "seeds.json") -> str:
        """Save discovered URLs to JSON with source tracking"""
        output_path = self.output_dir / filename

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
                'respect_per_source_config': True
            },
            'urls': sorted(list(self.all_urls)),
            'detailed_urls': flat_urls,
            'failed_domains': self.failed_domains
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"[SAVE] Seeds saved to JSON: {output_path}")
        logger.info(f"  Total URLs: {len(data['urls'])}")

        return str(output_path)

    def generate_sitemap_xml(self, filename: str = "master_seed.xml") -> str:
        """Generate XML sitemap respecting per-source discovery"""
        output_path = self.output_dir / filename

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

        tree = ET.ElementTree(urlset)
        tree.write(output_path, encoding='utf-8', xml_declaration=True)

        logger.info(f"[SAVE] XML Sitemap generated: {output_path}")
        logger.info(f"  Total URLs in sitemap: {len(self.all_urls)}")
        logger.info(f"  File size: {output_path.stat().st_size / 1024:.1f} KB")

        return str(output_path)

    def load_seeds(self, filename: str = "seeds.json") -> List[str]:
        """Load previously discovered seeds from file"""
        input_path = self.output_dir / filename

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
    """Run URL seeding with per-source configurations"""

    seeder = URLSeeder(
        source_domains=list(SOURCES.keys()),  # FIXED: Use .keys()
        output_dir="./data/raw/sitemap",
        global_query=None,  # Optional global query
        use_global_bm25=False
    )

    # Discover URLs respecting per-source configs
    discovered = await seeder.discover_urls(
        use_bm25_scoring=False,
        use_live_check=False
    )

    # Save results
    seeder.save_to_json("seeds.json")
    seeder.generate_sitemap_xml("master_seed.xml")

    logger.info("\n✓ URL seeding complete!")
    logger.info(f"  Total URLs discovered: {len(seeder.all_urls)}")
    logger.info(f"  Master sitemap: ./data/raw/sitemap/master_seed.xml")
    logger.info(f"  Seeds JSON: ./data/raw/sitemap/seeds.json")


if __name__ == "__main__":
    asyncio.run(main())