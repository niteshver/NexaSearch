import aiohttp
import PyPDF2
import argparse
import io
import asyncio
import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import trafilatura

from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.async_configs import BrowserConfig, CacheMode, CrawlerRunConfig, DefaultMarkdownGenerator
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
from crawl4ai import AsyncWebCrawler, CrawlerMonitor
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher, RateLimiter
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

from src.config.settings import settings
from src.crawler.logger import logger
from src.crawler.robots import RobotsParser
from src.crawler.utils import canonicalize_url


class CrawlerManager:
    def __init__(
        self,
        keywords: List[str] = None,
        max_pages: int = None,
        max_depth: int = None,
        deep_crawl: bool = False,
    ):
        self.keywords = keywords or settings.keywords_list
        self.max_pages = max_pages or settings.CRAWL_MAX_PAGES
        self.max_depth = max_depth or settings.CRAWL_MAX_DEPTH
        self.deep_crawl = deep_crawl
        self.robots_parser = RobotsParser()

    def select_markdown_text(self, result) -> str:
        """Prefer filtered markdown, then cited markdown, then raw markdown."""
        if not result.markdown:
            return ""
        candidates = [
            getattr(result.markdown, 'fit_markdown', None),
            getattr(result.markdown, 'markdown_with_citations', None),
            getattr(result.markdown, 'raw_markdown', None),
        ]
        for candidate in candidates:
            if candidate and str(candidate).strip():
                return str(candidate)
        return ""

    def has_crawl_error(self, result, markdown_text: str) -> bool:
        error_markers = [
            result.error_message or "",
            result.cleaned_html or "",
            markdown_text or "",
        ]
        return any("Crawl4AI Error:" in marker for marker in error_markers)

    async def crawl(self, urls: List[str]) -> List[Dict[str, Any]]:
        """Crawl a list of URLs. Handles both web pages and PDFs."""

        # Ensure output directories exist
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

        # 2. Separate PDFs and web URLs
        pdf_urls = [u for u in compliant_urls if urlparse(u).path.lower().endswith(".pdf")]
        web_urls = [u for u in compliant_urls if not urlparse(u).path.lower().endswith(".pdf")]

        logger.info(f"Crawling {len(compliant_urls)} URLs | Web: {len(web_urls)} | PDFs: {len(pdf_urls)}")

        # ===== PHASE 1: CRAWL WEB PAGES =====
        if web_urls:
            logger.info(f"\n[PHASE 1] Crawling {len(web_urls)} web pages...")

            browser_config = BrowserConfig(
                headless=True,
                verbose=False
            )

            markdown_generator = DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(
                    threshold=settings.PRUNING_THRESHOLD
                ),
                options={"ignore_links": True}
            )

            lowercase_keywords = [k.lower() for k in self.keywords]
            score = KeywordRelevanceScorer(
                keywords=lowercase_keywords,
                weight=0.6
            )

            strategy = None
            if self.deep_crawl and self.max_depth > 1:
                strategy = BFSDeepCrawlStrategy(
                    max_depth=self.max_depth,
                    include_external=False,
                    url_scorer=score,
                    max_pages=self.max_pages,
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
                    urls_total=len(web_urls),
                    refresh_rate=1.0,
                    enable_ui=True,
                ),
            )

            # WEB CONFIG ONLY (no PDF)
            config_run = CrawlerRunConfig(
                scraping_strategy=LXMLWebScrapingStrategy(),
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
            )

            async with AsyncWebCrawler(config=browser_config) as crawler:
                results = await crawler.arun_many(
                    urls=web_urls,
                    config=config_run,
                    dispatcher=dispatcher,
                )
                
                # arun_many may return an async generator or None
                if results is None:
                    logger.warning(f"arun_many returned None for {len(web_urls)} URLs")
                    results = []
                
                try:
                    async for result in results:
                        if not result.success:
                            logger.error(f"Crawl failed for {result.url}: {result.error_message}")
                            continue

                        markdown_text = self.select_markdown_text(result) if hasattr(result, 'markdown') and result.markdown else ""

                        if self.has_crawl_error(result, markdown_text):
                            logger.warning(f"Skipping page with crawl error: {result.url}")
                            continue

                        raw_html = getattr(result, "html", None) or getattr(result, "cleaned_html", None)
                        cleaned_content = trafilatura.extract(
                            raw_html,
                            output_format="markdown",
                            include_comments=False,
                            include_tables=True,
                        ) if raw_html else None

                        if not cleaned_content:
                            logger.warning(f"Trafilatura extraction failed {result.url}")
                            cleaned_content = markdown_text

                        metadata = result.metadata or {}
                        canonical_url = canonicalize_url(result.url)
                        filename = hashlib.md5(canonical_url.encode()).hexdigest()

                        # Save markdown
                        markdown_path = settings.absolute_db_path.parent / f"raw/markdown/{filename}.md"
                        with open(markdown_path, "w", encoding="utf-8") as f:
                            f.write(cleaned_content)

                        # Save JSON
                        doc_dict = {
                            "id": filename,
                            "url": result.url,
                            "canonical_url": canonical_url,
                            "title": metadata.get("title") or result.url,
                            "status": result.status_code,
                            "markdown": cleaned_content,
                            "markdown_length": len(cleaned_content),
                            "internal_links": result.links.get("internal", [])[:20] if hasattr(result, 'links') else [],
                            "external_links": result.links.get("external", [])[:20] if hasattr(result, 'links') else [],
                            "images": result.media.get("images", [])[:10] if hasattr(result, 'media') else [],
                            "metadata": metadata,
                            "crawled_at": datetime.now().isoformat(),
                            "type": "webpage"
                        }

                        json_path = settings.absolute_db_path.parent / f"raw/json/{filename}.json"
                        with open(json_path, "w", encoding="utf-8") as f:
                            json.dump(doc_dict, f, indent=4, ensure_ascii=False)

                        crawled_documents.append(doc_dict)
                        logger.info(f"✓ Crawled (webpage): {result.url}")
                except TypeError:
                    # arun_many may not be iterable; fallback to arun
                    logger.warning("arun_many did not return an async iterable; falling back to sequential arun()")
                    for url in web_urls:
                        try:
                            result = await crawler.arun(url=url, config=config_run)
                            if not result.success:
                                logger.error(f"Crawl failed for {url}: {result.error_message}")
                                continue

                            markdown_text = self.select_markdown_text(result) if hasattr(result, 'markdown') and result.markdown else ""

                            if self.has_crawl_error(result, markdown_text):
                                logger.warning(f"Skipping page with crawl error: {url}")
                                continue

                            raw_html = getattr(result, "html", None) or getattr(result, "cleaned_html", None)
                            cleaned_content = trafilatura.extract(
                                raw_html,
                                output_format="markdown",
                                include_comments=False,
                                include_tables=True,
                            ) if raw_html else None

                            if not cleaned_content:
                                logger.warning(f"Trafilatura extraction failed {url}")
                                cleaned_content = markdown_text

                            metadata = result.metadata or {}
                            canonical_url = canonicalize_url(result.url)
                            filename = hashlib.md5(canonical_url.encode()).hexdigest()

                            # Save markdown
                            markdown_path = settings.absolute_db_path.parent / f"raw/markdown/{filename}.md"
                            with open(markdown_path, "w", encoding="utf-8") as f:
                                f.write(cleaned_content)

                            # Save JSON
                            doc_dict = {
                                "id": filename,
                                "url": result.url,
                                "canonical_url": canonical_url,
                                "title": metadata.get("title") or result.url,
                                "status": result.status_code,
                                "markdown": cleaned_content,
                                "markdown_length": len(cleaned_content),
                                "internal_links": result.links.get("internal", [])[:20] if hasattr(result, 'links') else [],
                                "external_links": result.links.get("external", [])[:20] if hasattr(result, 'links') else [],
                                "images": result.media.get("images", [])[:10] if hasattr(result, 'media') else [],
                                "metadata": metadata,
                                "crawled_at": datetime.now().isoformat(),
                                "type": "webpage"
                            }

                            json_path = settings.absolute_db_path.parent / f"raw/json/{filename}.json"
                            with open(json_path, "w", encoding="utf-8") as f:
                                json.dump(doc_dict, f, indent=4, ensure_ascii=False)

                            crawled_documents.append(doc_dict)
                            logger.info(f"✓ Crawled (webpage): {result.url}")
                        except Exception as e:
                            logger.error(f"Exception crawling {url}: {e}")
                            continue

        # ===== PHASE 2: CRAWL PDFs =====
        if pdf_urls:
            logger.info(f"\n[PHASE 2] Crawling {len(pdf_urls)} PDFs...")

            for pdf_url in pdf_urls:
                try:
                    logger.info(f"Downloading PDF: {pdf_url}")

                    # Direct download
                    async with aiohttp.ClientSession() as session:
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                        }
                        async with session.get(pdf_url, timeout=30, headers=headers) as resp:
                            if resp.status == 200:
                                pdf_content = await resp.read()
                                canonical_url = canonicalize_url(pdf_url)
                                filename = hashlib.md5(canonical_url.encode()).hexdigest()

                                # Save PDF binary
                                pdf_path = settings.absolute_db_path.parent / f"raw/pdf/{filename}.pdf"
                                with open(pdf_path, "wb") as f:
                                    f.write(pdf_content)

                                file_size = len(pdf_content) / 1024
                                logger.info(f"  Saved PDF: {file_size:.1f}KB")

                                # Extract text using PyPDF2
                                try:
                                    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
                                    markdown_text = ""
                                    for page_num in range(len(pdf_reader.pages)):
                                        markdown_text += pdf_reader.pages[page_num].extract_text()
                                    logger.info(f"  Extracted: {len(markdown_text)} characters")
                                except Exception as e:
                                    logger.warning(f"  Text extraction failed: {e}")
                                    markdown_text = ""

                                # Save markdown
                                markdown_path = settings.absolute_db_path.parent / f"raw/markdown/{filename}.md"
                                with open(markdown_path, "w", encoding="utf-8") as f:
                                    f.write(markdown_text)

                                # Save JSON
                                doc_dict = {
                                    "id": filename,
                                    "url": pdf_url,
                                    "canonical_url": canonical_url,
                                    "title": pdf_url.split('/')[-1],
                                    "status": 200,
                                    "pdf_size_kb": file_size,
                                    "markdown": markdown_text,
                                    "markdown_length": len(markdown_text),
                                    "crawled_at": datetime.now().isoformat(),
                                    "type": "pdf"
                                }

                                json_path = settings.absolute_db_path.parent / f"raw/json/{filename}.json"
                                with open(json_path, "w", encoding="utf-8") as f:
                                    json.dump(doc_dict, f, indent=4, ensure_ascii=False)

                                crawled_documents.append(doc_dict)
                                logger.info(f"✓ Crawled (PDF): {pdf_url}")
                            else:
                                logger.error(f"PDF download failed: HTTP {resp.status}")

                except Exception as e:
                    logger.error(f"PDF crawl error for {pdf_url}: {e}")
                    continue

        # ===== DETAILED SUMMARY STATISTICS =====
        total_urls = len(compliant_urls)
        successful_urls = len(crawled_documents)
        failed_urls = total_urls - successful_urls
        
        webpages = sum(1 for result in crawled_documents if result.get('type') == 'webpage')
        pdfs = sum(1 for result in crawled_documents if result.get('type') == 'pdf')
        
        logger.info(f"\n{'='*70}")
        logger.info(f"CRAWLING SUMMARY")
        logger.info(f"{'='*70}")
        logger.info(f"Total URLs: {total_urls}")
        logger.info(f"  Web URLs: {len(web_urls)}")
        logger.info(f"  PDF URLs: {len(pdf_urls)}")
        logger.info(f"{'='*70}")
        logger.info(f"Successfully crawled: {successful_urls}")
        logger.info(f"  ✓ Web pages: {webpages}")
        logger.info(f"  ✓ PDFs: {pdfs}")
        logger.info(f"Failed: {failed_urls}")
        logger.info(f"Success rate: {(successful_urls/total_urls*100):.1f}%" if total_urls > 0 else "N/A")
        logger.info(f"{'='*70}\n")
        return crawled_documents


def _checkpoint_path() -> Path:
    """Return the location used to resume an interrupted sitemap crawl."""
    return settings.absolute_db_path.parent / ".crawler_checkpoint.json"


def _load_checkpoint(sitemap_path: Path, total_urls: int) -> int:
    """Return the next seed offset only when the checkpoint matches the sitemap."""
    path = _checkpoint_path()
    if not path.exists():
        return 0

    try:
        checkpoint = json.loads(path.read_text(encoding="utf-8"))
        if (
            checkpoint.get("sitemap") == str(sitemap_path.resolve())
            and checkpoint.get("total_urls") == total_urls
        ):
            return max(0, min(int(checkpoint.get("next_offset", 0)), total_urls))
    except (OSError, ValueError, TypeError) as exc:
        logger.warning(f"Ignoring unreadable crawler checkpoint: {exc}")
    return 0


def _save_checkpoint(sitemap_path: Path, total_urls: int, next_offset: int) -> None:
    """Atomically persist progress after each completed batch."""
    path = _checkpoint_path()
    payload = {
        "sitemap": str(sitemap_path.resolve()),
        "total_urls": total_urls,
        "next_offset": next_offset,
        "updated_at": datetime.now().isoformat(),
    }
    temporary_path = path.with_suffix(".tmp")
    temporary_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    temporary_path.replace(path)


async def main(
    sitemap_path: Path,
    limit: int | None,
    batch_size: int,
    max_pages: int,
    max_depth: int,
    resume: bool,
    follow_links: bool,
):
    if not sitemap_path.exists():
        logger.error(f"Sitemap file not found: {sitemap_path}")
        return
    if batch_size < 1:
        raise ValueError("--batch-size must be at least 1")
    if limit is not None and limit < 1:
        raise ValueError("--limit must be at least 1")

    tree = ET.parse(sitemap_path)
    urls = [
        loc.text.strip()
        for loc in tree.getroot().findall(".//{*}loc")
        if loc.text and loc.text.strip()
    ]
    if not urls:
        logger.error(f"No URLs found in sitemap: {sitemap_path}")
        return

    urls = urls[:limit] if limit is not None else urls
    logger.info(f"Loaded {len(urls)} seed URLs from sitemap.")

    manager = CrawlerManager(
        max_pages=max_pages,
        max_depth=max_depth,
        deep_crawl=follow_links,
    )
    start_offset = _load_checkpoint(sitemap_path, len(urls)) if resume else 0
    if start_offset:
        logger.info(f"Resuming after {start_offset} completed seed URLs.")

    for start in range(start_offset, len(urls), batch_size):
        batch = urls[start : start + batch_size]
        batch_number = start // batch_size + 1
        total_batches = (len(urls) + batch_size - 1) // batch_size
        logger.info(
            f"[BATCH {batch_number}/{total_batches}] Crawling seed URLs "
            f"{start + 1}-{start + len(batch)} of {len(urls)}"
        )

        # Individual files are saved by CrawlerManager before this returns. If
        # this batch fails, its checkpoint is not advanced and it is retried on
        # the next run. Existing URL-hash files are safe to overwrite.
        documents = await manager.crawl(batch)
        next_offset = start + len(batch)
        _save_checkpoint(sitemap_path, len(urls), next_offset)
        logger.info(
            f"[BATCH {batch_number}/{total_batches}] Saved {len(documents)} documents; "
            f"checkpointed at {next_offset}/{len(urls)} seed URLs."
        )

    logger.info(f"Sitemap crawl complete: {len(urls)} seed URLs processed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl URLs from a sitemap.")
    parser.add_argument(
        "--sitemap",
        type=Path,
        default=settings.BASE_DIR / "data/raw/sitemap/master_seed.xml",
    )
    parser.add_argument("--limit", type=int, help="Maximum sitemap URLs to crawl (default: all).")
    parser.add_argument("--batch-size", type=int, default=25, help="Seed URLs per saved batch (default: 25).")
    parser.add_argument("--max-pages", type=int, default=1, help="Pages per seed URL (default: 1).")
    parser.add_argument("--max-depth", type=int, default=1, help="Maximum crawl depth (default: 1).")
    parser.add_argument("--follow-links", action="store_true", help="Also deep-crawl links discovered from each sitemap URL.")
    parser.add_argument("--no-resume", action="store_true", help="Start from the beginning instead of using the checkpoint.")
    args = parser.parse_args()
    asyncio.run(
        main(
            args.sitemap,
            args.limit,
            args.batch_size,
            args.max_pages,
            args.max_depth,
            resume=not args.no_resume,
            follow_links=args.follow_links,
        )
    )
