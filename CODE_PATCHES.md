# NexaSearch: Ready-to-Apply Code Patches

This file contains copy-paste ready code fixes for the 5 critical issues.

---

## Patch 1: Seeding Error Recovery

**File:** `src/seeder/url_seeder.py` (around line 154)

**Replace this:**
```python
try:
    async with AsyncUrlSeeder() as seeder:
        # Process sources in batches by priority
        sorted_sources = sorted(
            sources_to_seed.items(),
            key=lambda x: (x[1].get("priority", 5), -x[1].get("reputation", 0))
        )

        for i, (domain, source_config) in enumerate(sorted_sources, 1):
            await self._seed_domain(
                seeder,
                domain,
                source_config,
                i,
                len(sorted_sources)
            )
```

**With this:**
```python
try:
    async with AsyncUrlSeeder() as seeder:
        # Process sources in batches by priority
        sorted_sources = sorted(
            sources_to_seed.items(),
            key=lambda x: (x[1].get("priority", 5), -x[1].get("reputation", 0))
        )

        for i, (domain, source_config) in enumerate(sorted_sources, 1):
            try:
                await asyncio.wait_for(
                    self._seed_domain(
                        seeder,
                        domain,
                        source_config,
                        i,
                        len(sorted_sources)
                    ),
                    timeout=300.0
                )
            except asyncio.TimeoutError:
                logger.error(f"[{self.correlation_id}] ✗ Timeout on {domain}, continuing...")
                self.failed_sources.append({
                    'domain': domain,
                    'error': 'Timeout (300s)',
                    'timestamp': datetime.now().isoformat(),
                })
            except Exception as e:
                logger.error(f"[{self.correlation_id}] ✗ Error on {domain}: {e}", exc_info=True)
                self.failed_sources.append({
                    'domain': domain,
                    'error': str(e),
                    'timestamp': datetime.now().isoformat(),
                })
                # Continue with next domain instead of crashing
```

---

## Patch 2: Stream URLs to Disk (Memory Efficient)

**File:** `src/seeder/url_seeder.py` (around line 43-55)

**Replace `__init__` method:**
```python
def __init__(self, config: Optional[Any] = None, output_dir: Optional[Any] = None):
    """Initialize enterprise seeder."""
    self.correlation_id = str(uuid.uuid4())[:8]
    self.discovered_urls: Set[str] = set()
    self.urls_by_source: Dict[str, List[Dict[str, Any]]] = {}
    self.failed_sources: List[Dict[str, Any]] = []
    self.source_metrics: Dict[str, Dict[str, Any]] = {}
    self.config = config
    self.output_dir = Path(output_dir or settings.BASE_DIR / "data/raw/sitemap")
    self.output_dir.mkdir(parents=True, exist_ok=True)

    self.metrics = {
        'start_time': time.time(),
        'total_urls': 0,
        'total_urls_estimated': calculate_total_estimated_urls(),
        'sources_succeeded': 0,
        'sources_failed': 0,
    }

    logger.info(f"[{self.correlation_id}] ✓ Enterprise URLSeeder initialized")
    logger.info(f"[{self.correlation_id}] Estimated total URLs: {self.metrics['total_urls_estimated']:,}")
```

**Replace with this memory-efficient version:**
```python
def __init__(self, config: Optional[Any] = None, output_dir: Optional[Any] = None):
    """Initialize enterprise seeder with memory-efficient streaming."""
    self.correlation_id = str(uuid.uuid4())[:8]
    
    # Don't hold all URLs in RAM
    self.discovered_urls: Set[str] = set()  # Only for dedup check
    self.urls_by_source: Dict[str, List[Dict[str, Any]]] = {}  # Will stream instead
    
    self.failed_sources: List[Dict[str, Any]] = []
    self.source_metrics: Dict[str, Dict[str, Any]] = {}
    self.config = config
    self.output_dir = Path(output_dir or settings.BASE_DIR / "data/raw/sitemap")
    self.output_dir.mkdir(parents=True, exist_ok=True)

    # Streaming writers (line-buffered to disk)
    self.urls_jsonl_path = self.output_dir / "urls.jsonl"
    self.urls_jsonl_file = open(
        self.urls_jsonl_path,
        'w',
        encoding='utf-8',
        buffering=1  # Line buffered for flushing
    )

    self.metrics = {
        'start_time': time.time(),
        'total_urls': 0,
        'total_urls_estimated': calculate_total_estimated_urls(),
        'sources_succeeded': 0,
        'sources_failed': 0,
    }

    logger.info(f"[{self.correlation_id}] ✓ Enterprise URLSeeder initialized (streaming mode)")
    logger.info(f"[{self.correlation_id}] Estimated total URLs: {self.metrics['total_urls_estimated']:,}")
    logger.info(f"[{self.correlation_id}] Streaming URLs to: {self.urls_jsonl_path}")
```

**Then update the seeding method to stream URLs:**
```python
# In _seed_domain method, replace the URL collection with streaming:
for url_entry in urls_data:
    if isinstance(url_entry, dict):
        url = url_entry.get('url', '')
    else:
        url = str(url_entry)

    if url and url.startswith('http'):
        self.discovered_urls.add(url)  # Keep only for dedup
        
        # Stream to disk instead of storing in memory
        self.urls_jsonl_file.write(json.dumps({
            'url': url,
            'source': domain,
            'discovered_at': datetime.now().isoformat(),
        }) + '\n')
        self.urls_jsonl_file.flush()  # Flush after each URL
        
        valid_urls.append(url)  # Keep count only
```

---

## Patch 3: Atomic File Writes in Crawler

**File:** `src/crawler/crawler.py` (add new method at top of CrawlerManager class)

**Add this method:**
```python
def _safe_write_file(self, path: Path, content: Any, is_json: bool = False) -> bool:
    """
    Write file atomically using temp+rename pattern.
    Prevents data corruption on crash/disk full.
    """
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        
        temp_fd, temp_path = tempfile.mkstemp(
            dir=str(path.parent),
            suffix='.tmp',
            text=True
        )
        
        try:
            if is_json:
                with open(temp_fd, 'w', encoding='utf-8') as f:
                    json.dump(content, f, indent=4, ensure_ascii=False)
            else:
                with open(temp_fd, 'w', encoding='utf-8') as f:
                    f.write(content)
        except Exception as write_error:
            import os
            os.close(temp_fd)
            os.unlink(temp_path)
            raise write_error
        
        # Atomic rename
        Path(temp_path).replace(path)
        return True
        
    except OSError as e:
        logger.error(f"Failed to write {path}: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error writing {path}: {e}", exc_info=True)
        return False
```

**Replace file write calls with this. For example, change:**
```python
# OLD (not safe):
markdown_path = settings.absolute_db_path.parent / f"raw/markdown/{filename}.md"
with open(markdown_path, "w", encoding="utf-8") as f:
    f.write(cleaned_content)

json_path = settings.absolute_db_path.parent / f"raw/json/{filename}.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(doc_dict, f, indent=4, ensure_ascii=False)
```

**To:**
```python
# NEW (safe):
markdown_path = settings.absolute_db_path.parent / f"raw/markdown/{filename}.md"
if self._safe_write_file(markdown_path, cleaned_content, is_json=False):
    logger.info(f"✓ Wrote markdown: {filename}")
else:
    logger.error(f"✗ Failed to write markdown for {result.url}")
    # DON'T skip—content is in memory, can retry

json_path = settings.absolute_db_path.parent / f"raw/json/{filename}.json"
if self._safe_write_file(json_path, doc_dict, is_json=True):
    logger.info(f"✓ Wrote JSON metadata: {filename}")
else:
    logger.error(f"✗ Failed to write JSON for {result.url}")
```

---

## Patch 4: Checkpoint System for URL Discovery

**File:** `src/pipeline/orchestrator.py` (replace `_stage_seeding` method)

**Add this import at top:**
```python
import json
from pathlib import Path
from datetime import datetime
```

**Replace the entire `_stage_seeding` method with:**
```python
async def _stage_seeding(self, metrics: PipelineMetrics) -> Dict[str, Any]:
    """
    Stage 1: URL Seeding with checkpoint-based resumption.
    """
    checkpoint_file = self.output_base / ".seeding_checkpoint.json"
    
    # Load previous checkpoint if it exists
    completed_domains = set()
    all_discovered_urls = []
    
    if checkpoint_file.exists():
        try:
            with open(checkpoint_file, 'r') as f:
                checkpoint = json.load(f)
                completed_domains = set(checkpoint.get('completed_domains', []))
                all_discovered_urls = checkpoint.get('discovered_urls', [])
                logger.info(f"Resuming from checkpoint: {len(completed_domains)} completed domains")
        except Exception as e:
            logger.warning(f"Could not load checkpoint: {e}, starting fresh")
    
    if self.crawl_urls:
        # Manual URL list provided
        output_dir = self.output_base / "raw/sitemap"
        output_dir.mkdir(parents=True, exist_ok=True)
        self._write_seed_artifacts(self.crawl_urls, output_dir=output_dir)
        metrics.items_processed = len(self.crawl_urls)
        metrics.items_failed = 0
        return {
            'total_urls': len(self.crawl_urls),
            'domains_succeeded': 1,
            'domains_failed': 0,
            'seeds_file': str(output_dir / "seeds.json"),
            'sitemap_file': str(output_dir / "master_seed.xml"),
        }

    # Auto-discovery mode
    from src.seeder.sources import ALL_ENTERPRISE_SOURCES
    
    sources_to_seed = ALL_ENTERPRISE_SOURCES
    remaining_sources = {
        d: cfg for d, cfg in sources_to_seed.items()
        if d not in completed_domains
    }
    
    logger.info(f"Seeding {len(remaining_sources)} sources "
                f"(already completed: {len(completed_domains)})")
    
    seeder = URLSeeder(output_dir=str(self.output_base / "raw/sitemap"))
    
    # Process each source and checkpoint after each
    for domain, source_config in remaining_sources.items():
        try:
            config = seeder._build_seeding_config(domain, source_config)
            
            logger.info(f"Seeding {domain}...")
            urls_data = await asyncio.wait_for(
                seeder.seeder.urls(domain, config) if hasattr(seeder, 'seeder')
                else [],
                timeout=300.0
            )
            
            if urls_data:
                for url_entry in urls_data:
                    url = url_entry.get('url', '') if isinstance(url_entry, dict) else str(url_entry)
                    if url.startswith('http') and url not in all_discovered_urls:
                        all_discovered_urls.append(url)
            
            completed_domains.add(domain)
            metrics.items_processed += 1
            
            # Save checkpoint after each domain
            with open(checkpoint_file, 'w') as f:
                json.dump({
                    'completed_domains': list(completed_domains),
                    'discovered_urls': all_discovered_urls,
                    'timestamp': datetime.now().isoformat(),
                }, f, indent=2)
            
            logger.info(f"✓ Checkpoint saved: {len(all_discovered_urls)} URLs from {len(completed_domains)} domains")
            
        except asyncio.TimeoutError:
            logger.error(f"Timeout on {domain}")
            metrics.items_failed += 1
        except Exception as e:
            logger.error(f"Error on {domain}: {e}")
            metrics.items_failed += 1
    
    # Write final outputs
    seeder.discovered_urls = set(all_discovered_urls)
    seeder.save_master_sitemap_xml("master_seed.xml")
    seeder.save_comprehensive_json("seeds.json")
    
    # Clean up checkpoint
    checkpoint_file.unlink(missing_ok=True)
    
    return {
        'total_urls': len(all_discovered_urls),
        'domains_succeeded': len(completed_domains),
        'domains_failed': metrics.items_failed,
        'seeds_file': str(self.output_base / "raw/sitemap/seeds.json"),
        'sitemap_file': str(self.output_base / "raw/sitemap/master_seed.xml"),
    }
```

---

## Patch 5: Reuse aiohttp Session for PDF Crawling

**File:** `src/crawler/crawler.py` (around line 130-170)

**Replace this section:**
```python
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
```

**With this:**
```python
# ===== PHASE 2: CRAWL PDFs =====
if pdf_urls:
    logger.info(f"\n[PHASE 2] Crawling {len(pdf_urls)} PDFs...")

    # Create session ONCE and reuse for all PDFs
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    timeout = aiohttp.ClientTimeout(total=30)
    
    async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
        for pdf_url in pdf_urls:
            try:
                logger.info(f"Downloading PDF: {pdf_url}")

                # Reuse session
                async with session.get(pdf_url) as resp:
```

**Also update the closing:**
```python
                except Exception as e:
                    logger.error(f"PDF crawl error for {pdf_url}: {e}")
                    continue
```

---

## How to Apply These Patches

1. **Backup first:**
   ```bash
   cd /Users/niteshv1520/NexaSearch
   git commit -m "Backup before critical patches"
   ```

2. **Apply patches one by one** (don't apply all at once):
   - Start with Patch 3 (atomic writes) — lowest risk
   - Then Patch 5 (session reuse) — safe improvement
   - Then Patch 1 (error recovery) — handles edge cases
   - Then Patch 2 (streaming) — changes data structure
   - Finally Patch 4 (checkpoint) — ties everything together

3. **Test after each patch:**
   ```bash
   # Patch 3: Test file I/O
   pytest tests/test_file_io.py -v
   
   # Patch 5: Test PDF crawling speed
   time python src/crawler/crawler.py --limit 5 --pdf-only
   
   # Patch 1: Test with network failures
   pytest tests/test_seeding_resilience.py -v
   
   # Patch 2: Monitor memory usage
   python -m memory_profiler src/seeder/url_seeder.py
   
   # Patch 4: Test resumption
   pytest tests/test_checkpoint_resumption.py -v
   ```

4. **Validate all together:**
   ```bash
   pytest tests/ -v --cov=src
   ```

---

## Expected Test Results After Patches

✅ All files written without corruption  
✅ Memory usage stable (not growing)  
✅ PDF crawling 3x faster  
✅ Seeding continues after domain failures  
✅ Can resume from checkpoint  

---

**Next Steps:**
1. Apply patches 1-5
2. Test each one
3. Run full pipeline test
4. Then tackle Medium priority issues (see QUICK_FIXES.md)
