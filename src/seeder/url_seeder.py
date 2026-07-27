"""
URL Seeder Module - Production Grade
Uses Crawl4AI AsyncUrlSeeder for intelligent URL discovery
Generates master_seed.xml sitemap
Integrates with source module for seed domains
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import List, Set, Dict, Any
from pathlib import Path
import xml.etree.ElementTree as ET

from crawl4ai import AsyncUrlSeeder, SeedingConfig
from src.config.settings import settings
from src.crawler.logger import logger
from src.seeder.sources import SOURCES

logger = logging.getLogger(__name__)


def configured_source_domains() -> List[str]:
    """Return unique domains configured in the project's source catalogue."""
    return list(dict.fromkeys(
        domain
        for source in SOURCES.values()
        for domain in source["domains"]
    ))


class URLSeeder:
    """
    Production-grade URL seeder using Crawl4AI AsyncUrlSeeder.
    - Discovers URLs from source domains via sitemap + Common Crawl
    - Filters by relevance using BM25 scoring
    - Generates master_seed.xml sitemap
    - Saves discovered URLs to JSON
    """

    def __init__(
        self,
        source_domains: List[str] = None,
        output_dir: str = "./data/raw/sitemap",
        max_urls_per_domain: int = 1000,
        min_relevance_score: float = 0.3
    ):
        """
        Initialize URL Seeder.

        Args:
            source_domains: List of domains to seed from
            output_dir: Directory to save sitemap and seeds
            max_urls_per_domain: Maximum URLs per domain
            min_relevance_score: Minimum BM25 score (0-1)
        """
        self.source_domains = source_domains or configured_source_domains()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.max_urls_per_domain = max_urls_per_domain
        self.min_relevance_score = min_relevance_score

        self.discovered_urls: Dict[str, List[Dict[str, Any]]] = {}
        self.all_urls: Set[str] = set()
        self.failed_domains: List[Dict[str, str]] = []
        self.statistics = {}

    async def discover_urls(
        self,
        query: str = None,
        use_live_check: bool = False,
        use_bm25_scoring: bool = True
    ) -> Dict[str, List[str]]:
        """
        Discover URLs from source domains using Crawl4AI AsyncUrlSeeder.

        Args:
            query: BM25 search query for relevance scoring (optional)
            use_live_check: Verify URLs are accessible
            use_bm25_scoring: Use BM25 relevance scoring

        Returns:
            Dictionary mapping domains to lists of discovered URLs
        """
        logger.info(f"\n{'='*80}")
        logger.info(f"[URL SEEDER] Starting URL discovery from {len(self.source_domains)} domains")
        logger.info(f"{'='*80}")
        logger.info(f"Source domains: {', '.join(self.source_domains)}")
        logger.info(f"Max URLs per domain: {self.max_urls_per_domain}")
        logger.info(f"BM25 scoring: {use_bm25_scoring}")
        logger.info(f"Live check: {use_live_check}")
        if query:
            logger.info(f"Search query: {query}")
        logger.info(f"{'='*80}\n")

        try:
            async with AsyncUrlSeeder() as seeder:

                for i, domain in enumerate(self.source_domains, 1):
                    logger.info(f"\n[{i}/{len(self.source_domains)}] Seeding: {domain}")
                    logger.info(f"{''*80}")

                    try:
                        # Configure seeding strategy
                        config = SeedingConfig(
                            source="sitemap+cc",            # Sitemap + Common Crawl
                            extract_head=True,              # Extract page metadata
                            pattern="*",                    # Match all URLs
                            query=query if use_bm25_scoring else None,  # Search query
                            scoring_method="bm25" if use_bm25_scoring else None,  # BM25 scoring
                            score_threshold=self.min_relevance_score if use_bm25_scoring else None,
                            max_urls=self.max_urls_per_domain,  # Per domain limit
                            concurrency=20,                 # 20 parallel workers
                            hits_per_sec=10,                # Rate limiting
                            live_check=use_live_check,      # Verify accessibility
                            force=False,                    # Use cache
                            verbose=False,
                            filter_nonsense_urls=True,      # Filter admin/api/tracking
                            cache_ttl_hours=24              # Cache for 24 hours
                        )

                        # Discover URLs
                        logger.info(f"  Discovering URLs from sitemap and Common Crawl...")
                        urls_data = await seeder.urls(domain, config)

                        # Process and filter results
                        valid_urls = []
                        live_count = 0
                        dead_count = 0
                        low_score_count = 0

                        for url_entry in urls_data:
                            url = url_entry.get('url')
                            status = url_entry.get('status', 'unknown')
                            score = url_entry.get('relevance_score', 1.0)
                            head_data = url_entry.get('head_data', {})

                            # Skip invalid URLs
                            if not url or status == 'not_valid':
                                dead_count += 1
                                continue

                            # Skip low-scoring URLs (if BM25 enabled)
                            if use_bm25_scoring and score < self.min_relevance_score:
                                low_score_count += 1
                                continue

                            live_count += 1
                            valid_urls.append({
                                'url': url,
                                'status': status,
                                'score': score,
                                'title': head_data.get('title', ''),
                                'description': head_data.get('meta', {}).get('description', ''),
                                'discovered_at': datetime.now().isoformat()
                            })
                            self.all_urls.add(url)

                        # Store results
                        self.discovered_urls[domain] = valid_urls

                        # Log statistics
                        logger.info(f"  ✓ Discovery complete:")
                        logger.info(f"    • Valid URLs: {live_count}")
                        logger.info(f"    • Dead URLs: {dead_count}")
                        if use_bm25_scoring:
                            logger.info(f"    • Low relevance (filtered): {low_score_count}")
                        logger.info(f"    • Unique URLs added: {len(valid_urls)}")

                        # Rate limiting between domains
                        await asyncio.sleep(1)

                    except Exception as e:
                        logger.error(f"  ✗ Error seeding {domain}: {str(e)}")
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
            logger.error(f"\n✗ Fatal error in URL discovery: {str(e)}")
            raise

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

        if self.source_domains:
            avg_urls = total_urls / len(self.source_domains) if successful_domains > 0 else 0
            logger.info(f"Average URLs per domain: {avg_urls:.0f}")
        logger.info(f"{'='*80}\n")

    def save_to_json(self, filename: str = "seeds.json") -> str:
        """
        Save discovered URLs to JSON file.

        Args:
            filename: Output filename

        Returns:
            Path to saved file
        """
        output_path = self.output_dir / filename

        # Flatten URLs for easier access
        flat_urls = []
        for domain, urls in self.discovered_urls.items():
            flat_urls.extend(urls)

        data = {
            'metadata': {
                'total_urls': len(self.all_urls),
                'domains_seeded': len(self.discovered_urls),
                'domains_failed': len(self.failed_domains),
                'discovered_at': datetime.now().isoformat(),
                'source_domains': self.source_domains
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
        """
        Generate XML sitemap from discovered URLs.
        Follows XML sitemap protocol (www.sitemaps.org).

        Args:
            filename: Output XML filename

        Returns:
            Path to generated sitemap
        """
        output_path = self.output_dir / filename

        # Create root element
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

        # Add each URL
        for url in sorted(self.all_urls):
            url_elem = ET.SubElement(urlset, 'url')

            # <loc>
            loc = ET.SubElement(url_elem, 'loc')
            loc.text = url

            # <lastmod>
            lastmod = ET.SubElement(url_elem, 'lastmod')
            lastmod.text = datetime.now().isoformat()

            # <changefreq>
            changefreq = ET.SubElement(url_elem, 'changefreq')
            changefreq.text = 'weekly'

            # <priority>
            priority = ET.SubElement(url_elem, 'priority')
            priority.text = '0.8'

        # Create tree and write
        tree = ET.ElementTree(urlset)
        tree.write(output_path, encoding='utf-8', xml_declaration=True)

        logger.info(f"[SAVE] XML Sitemap generated: {output_path}")
        logger.info(f"  Total URLs in sitemap: {len(self.all_urls)}")
        logger.info(f"  File size: {output_path.stat().st_size / 1024:.1f} KB")

        return str(output_path)

    def generate_sitemap_index(self, filename: str = "sitemap_index.xml", urls_per_file: int = 50000) -> str:
        """
        Generate XML sitemap index for large URL collections.
        Useful when you have more than 50,000 URLs.

        Args:
            filename: Output index filename
            urls_per_file: URLs per individual sitemap

        Returns:
            Path to sitemap index
        """
        output_path = self.output_dir / filename

        # Split URLs into chunks
        url_list = sorted(list(self.all_urls))
        chunks = [url_list[i:i + urls_per_file] for i in range(0, len(url_list), urls_per_file)]

        # Generate individual sitemaps
        sitemaps = []
        for i, chunk in enumerate(chunks, 1):
            sitemap_name = f"sitemap_{i}.xml"
            sitemap_path = self.output_dir / sitemap_name

            # Create sitemap
            urlset = ET.Element('urlset')
            urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

            for url in chunk:
                url_elem = ET.SubElement(urlset, 'url')
                loc = ET.SubElement(url_elem, 'loc')
                loc.text = url
                lastmod = ET.SubElement(url_elem, 'lastmod')
                lastmod.text = datetime.now().isoformat()

            tree = ET.ElementTree(urlset)
            tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
            sitemaps.append(sitemap_name)

        # Generate index
        sitemapindex = ET.Element('sitemapindex')
        sitemapindex.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

        for sitemap_name in sitemaps:
            sitemap_elem = ET.SubElement(sitemapindex, 'sitemap')
            loc = ET.SubElement(sitemap_elem, 'loc')
            loc.text = f"{self.output_dir.name}/{sitemap_name}"
            lastmod = ET.SubElement(sitemap_elem, 'lastmod')
            lastmod.text = datetime.now().isoformat()

        tree = ET.ElementTree(sitemapindex)
        tree.write(output_path, encoding='utf-8', xml_declaration=True)

        logger.info(f"[SAVE] Sitemap index generated: {output_path}")
        logger.info(f"  Total sitemaps: {len(sitemaps)}")
        logger.info(f"  Total URLs: {len(self.all_urls)}")

        return str(output_path)

    def load_seeds(self, filename: str = "seeds.json") -> List[str]:
        """
        Load previously discovered seeds from file.

        Args:
            filename: JSON file to load

        Returns:
            List of URLs
        """
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
    """
    Example usage - Run URL seeding and generate sitemaps
    """

    # Initialize seeder with your source domains
    seeder = URLSeeder(
        output_dir="./data/raw/sitemap",
        max_urls_per_domain=500,
        min_relevance_score=0.3
    )

    # Discover URLs with optional BM25 relevance scoring
    discovered = await seeder.discover_urls(
        query="python tutorial guide",  # Optional: BM25 search query
        use_live_check=False,           # Check if URLs are accessible
        use_bm25_scoring=True           # Use relevance scoring
    )

    # Save results
    seeder.save_to_json("seeds.json")
    seeder.generate_sitemap_xml("master_seed.xml")

    # If you have many URLs (>50k), generate sitemap index
    # seeder.generate_sitemap_index("sitemap_index.xml")

    logger.info("\n✓ URL seeding complete!")
    logger.info(f"  Master sitemap: ./data/raw/sitemap/master_seed.xml")
    logger.info(f"  Seeds JSON: ./data/raw/sitemap/seeds.json")


if __name__ == "__main__":
    
    asyncio.run(main())
