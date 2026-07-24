import asyncio
import os
import json
import hashlib
from datetime import datetime
from typing import List, Dict, Any

import xml.etree.ElementTree as ET

from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.async_configs import BrowserConfig, CacheMode, CrawlerRunConfig, DefaultMarkdownGenerator
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
from crawl4ai import AsyncWebCrawler, CrawlerMonitor
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher, RateLimiter
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.processors.pdf import PDFCrawlerStrategy, PDFContentScrapingStrategy

from src.config.settings import settings
from src.crawler.logger import logger
from src.crawler.robots import RobotsParser
from src.crawler.utils import canonicalize_url

class CrawlerManager:
    def __init__(self, keywords: List[str] = None, max_pages: int = None, max_depth: int = None):
        self.keywords = keywords or settings.keywords_list
        self.max_pages = max_pages or settings.CRAWL_MAX_PAGES
        self.max_depth = max_depth or settings.CRAWL_MAX_DEPTH
        self.robots_parser = RobotsParser()

    def select_markdown_text(self, result) -> str:
        """Prefer filtered markdown, then cited markdown, then raw markdown."""
        if not result.markdown:
            return ""

        candidates = [
            result.markdown.fit_markdown,
            result.markdown.markdown_with_citations,
            result.markdown.raw_markdown,
        ]
        for candidate in candidates:
            if candidate and candidate.strip():
                return candidate
        return ""

    def has_crawl_error(self, result, markdown_text: str) -> bool:
        error_markers = [
            result.error_message or "",
            result.cleaned_html or "",
            markdown_text or "",
        ]
        return any("Crawl4AI Error:" in marker for marker in error_markers)

    

    async def crawl(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Crawl a list of URLs concurrently using Crawl4AI.
        """
        # Ensure outputs directories exist
        os.makedirs(settings.absolute_db_path.parent / "raw/markdown", exist_ok=True)
        os.makedirs(settings.absolute_db_path.parent / "raw/json", exist_ok=True)
        os.makedirs(settings.absolute_db_path.parent / "raw/pdf", exist_ok=True)

        crawled_documents = []

        # 1. Filter URLs by robots.txt compliance
        compliant_urls = []
        for url in urls:
            if await self.robots_parser.is_allowed(url):
                compliant_urls.append(url)
            else:
                logger.warning(f"URL skipped due to robots.txt restrictions: {url}")
        
        if not compliant_urls:
            logger.warning("No URLs remaining after robots.txt check.")
            return []

        logger.info(f"Crawling {len(compliant_urls)} URLs with Crawl4AI...")

        browser_config = BrowserConfig(
            headless=True,
            verbose=False
        )

        markdown_generator = DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(
                threshold=settings.PRUNING_THRESHOLD
            ),
            options={
                "ignore_links": True
            }
        )

        # Build keywords scorer (lower-case list)
        lowercase_keywords = [k.lower() for k in self.keywords]
        score = KeywordRelevanceScorer(
            keywords=lowercase_keywords,
            weight=0.6
        )

        strategy = BFSDeepCrawlStrategy(
            max_depth=self.max_depth,
            include_external=False,
            url_scorer=score,
            max_pages=self.max_pages
        )

        dispatcher = MemoryAdaptiveDispatcher(
            memory_threshold_percent=90.0,
            check_interval=1.0,
            max_session_permit=settings.CRAWL_CONCURRENT,
            rate_limiter=RateLimiter(
                base_delay=(1.0, 2.0),
                max_delay=30.0,
                max_retries=settings.MAX_RETRIES
            ),
            monitor=CrawlerMonitor(
                urls_total=len(compliant_urls),
                refresh_rate=1.0,
                enable_ui=True                 # Allow Crawling to display
            )
        )
        pdf_scraping_cfg = PDFContentScrapingStrategy(
                extract_images=True,
                save_images_locally=True,
                #image_save_dir=image_output_dir,
                batch_size=2
                )
    
        config_run = CrawlerRunConfig(
            wait_until=settings.WAIT_UNTIL,
            max_retries=settings.MAX_RETRIES,
            markdown_generator=markdown_generator,
            deep_crawl_strategy=strategy,
            stream=True,
            word_count_threshold=settings.WORD_COUNT_THRESHOLD,
            exclude_external_links=True,
            exclude_social_media_links=True,
            process_iframes=True,
            remove_forms=True,
            cache_mode=CacheMode.BYPASS,
            magic=True,
            scraping_strategy=pdf_scraping_cfg,
        )

        async with AsyncWebCrawler(config=browser_config) as crawler:
            async for result in crawler.arun_many(
                urls=compliant_urls,
                config=config_run,
                dispatcher=dispatcher,
            ):
                if not result.success:
                    logger.error(f"Crawl failed for {result.url}: {result.error_message}")
                    continue

                markdown_text = self.select_markdown_text(result) if hasattr(result, 'markdown') and result.markdown else ""

                if self.has_crawl_error(result, markdown_text):
                    logger.warning(f"Skipping page with crawl error: {result.url}")
                    continue

                metadata = result.metadata or {}
                
                # Canonicalize URL for naming and consistency
                canonical_url = canonicalize_url(result.url)
                filename = hashlib.md5(canonical_url.encode()).hexdigest()

                # Save raw files to disk
                markdown_path = settings.absolute_db_path.parent / f"raw/markdown/{filename}.md"
                with open(markdown_path, "w", encoding="utf-8") as f:
                    f.write(markdown_text)

                if hasattr(result, 'pdf_content') and result.pdf_content:
                    pdf_path = settings.absolute_db_path.parent / f"raw/pdf/{filename}.pdf"
                    with open(pdf_path, "wb") as f:
                        f.write(result.pdf_content)

                doc_dict = {
                    "id": filename,
                    "url": result.url,
                    "canonical_url": canonical_url,
                    "title": metadata.get("title") or result.url,
                    "status": result.status_code,
                    "markdown": markdown_text,
                    "internal_links": result.links.get("internal", []),
                    "external_links": result.links.get("external", []),
                    "images": result.media.get("images", []),
                    "metadata": metadata,
                    "crawled_at": datetime.now().isoformat()
                }

                json_path = settings.absolute_db_path.parent / f"raw/json/{filename}.json"
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(doc_dict, f, indent=4, ensure_ascii=False)

                crawled_documents.append(doc_dict)
                logger.info(f"Successfully crawled and saved raw data for: {result.url}")

        return crawled_documents

async def main():
    sitemap_path = settings.BASE_DIR / "data/raw/sitemap/master_seed.xml"
    if not sitemap_path.exists():
        logger.error(f"Sitemap file not found: {sitemap_path}")
        return

    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls = []
    for loc in root.findall(".//{*}loc"):
        if loc.text and loc.text.strip():
            urls.append(loc.text.strip())

    if not urls:
        logger.error(f"No URLs found in sitemap: {sitemap_path}")
        return

    logger.info(f"Loaded {len(urls)} seed URLs from sitemap.")
    manager = CrawlerManager()
    await manager.crawl(urls[:10])  # Crawl first 10 for test run

if __name__ == "__main__":
    asyncio.run(main())
