## Data Processing

To ensure high-quality search results, NexaSearch processes documents through multiple stages before they are indexed.

### During Crawling

During the crawling stage, we extract the main content and remove unnecessary information from web pages.

- HTML content extraction
- Header & footer removal
- Navigation menu removal
- Advertisement removal
- Cookie banners & pop-ups removal
- Boilerplate content removal
- Basic metadata extraction
- PII and sensitive content filtering *(planned)*

---

### Post-Processing

After crawling, documents go through additional processing to improve search quality.

- URL canonicalization
- Exact duplicate detection (SHA-256)
- Near-duplicate detection (MinHash + LSH)
- Quality classification (DistilRoBERTa)
- Document chunking
- Metadata enrichment
- Embedding generation
- BM25 index generation
- Vector index generation
- Cross-encoder reranking

---

### Processing Pipeline

```text
Raw Document
      │
      ▼
Content Extraction
      │
      ▼
Cleaning & Boilerplate Removal
      │
      ▼
Canonicalization
      │
      ▼
Duplicate Detection
      │
      ▼
Quality Classification
      │
      ▼
Chunking
      │
      ▼
Metadata Extraction
      │
      ▼
BM25 + Embeddings
      │
      ▼
Indexing
```


