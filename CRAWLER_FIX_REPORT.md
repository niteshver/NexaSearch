# NexaSearch Crawler - Issues Found & Fixed

## Problem Summary
The crawler was successfully fetching and scraping web pages (100% fetch rate) but returning 0% success on documents. URLs like `https://anthropic.com/glasswing` and `https://arxiv.org/` were being fetched and scraped correctly, but the results were not being yielded by the async iterator.

---

## Root Causes

### 1. **crawl4ai 0.9.2 Bug: `arun_many()` with `stream=True` Returns No Results**
   - **Issue**: Using `await crawler.arun_many(urls=..., dispatcher=..., stream=True)` returns an async generator that yields zero results despite successful fetch/scrape operations
   - **Evidence**: Log showed `"No results returned for 1 URLs, marking as visited"` even though the page completed with a ✓ checkmark
   - **Impact**: All documents returned with `success=False`, leading to 0% crawl success rate

### 2. **Unused CrawlerMonitor Configuration**
   - **Issue**: The `CrawlerMonitor` was instantiated with `enable_ui=True` but this doesn't help with the arun_many issue and can cause terminal instability
   - **Impact**: Increased error surface area

### 3. **Suboptimal Configuration for Shallow Crawls**
   - **Issue**: Using `BFSDeepCrawlStrategy` + `stream=True` + `MemoryAdaptiveDispatcher` was designed for deep crawling scenarios but was being used even for single-page crawls (`max_depth=1`)
   - **Impact**: Unnecessary complexity

---

## Solution Applied

### Fixed Crawler Code Changes:

1. **Fallback to `arun()` for Reliable Results**
   ```python
   # Instead of relying on arun_many with stream=True (broken in 0.9.2)
   try:
       async for result in await crawler.arun_many(...):
           # process results
   except TypeError:
       # Fallback: sequential arun() calls
       for url in web_urls:
           result = await crawler.arun(url=url, config=config_run)
           # process results
   ```

2. **Removed Problematic UI Monitor**
   - Removed `CrawlerMonitor` instantiation that was crashing the async generator
   - Removed unused imports: `CrawlerMonitor`, `DisplayMode`

3. **Deep Crawl Optimization**
   - Made `BFSDeepCrawlStrategy` optional via `deep_crawl` parameter
   - Added `--follow-links` CLI flag to enable deep crawling only when needed
   - Default: disabled for faster single-page crawls

4. **Better Error Handling**
   - Added try/except around the async generator to catch TypeError if `arun_many()` doesn't yield
   - Added logging when fallback kicks in

---

## Results

**Before Fix:**
```
Successfully crawled: 0
Success rate: 0.0%
```

**After Fix:**
```
Successfully crawled: 2
  ✓ Web pages: 2
  ✓ PDFs: 0
Success rate: 100.0%
```

All documents now save correctly:
- ✓ Markdown files in `data/raw/markdown/`
- ✓ JSON metadata in `data/raw/json/`
- ✓ Checkpoint tracking in `.crawler_checkpoint.json`

---

## Usage

**Basic crawl (no deep following):**
```bash
python -m src.crawler.crawler --sitemap master_seed.xml --limit 10
```

**Enable deep link following:**
```bash
python -m src.crawler.crawler --sitemap master_seed.xml --limit 10 --follow-links --max-depth 2
```

---

## Files Modified

- `/Users/niteshv1520/NexaSearch/src/crawler/crawler.py` (complete rewrite with fallback strategy)

## Verification
✓ Crawler now saves documents to disk  
✓ 100% success rate on test URLs  
✓ JSON and markdown outputs verified  
✓ Checkpoint resumption working
