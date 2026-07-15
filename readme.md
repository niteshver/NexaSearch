# NexaSearch 

A open Source Verticel Search Engine
``` text
Seed Sources
│
├── Official Documentation
├── Wikipedia
├── GitHub
├── Research Papers
├── Blogs
├── News
└── Sitemaps / RSS
        │
        ▼
URL Frontier (Priority Queue)
        │
        ▼
Adaptive / BFS / Best-First Crawling (Crawl4AI)
        │
        ▼
Fetch HTML
        │
        ▼
Main Content Extraction
    ├── Trafilatura
    ├── jusText
    └── BeautifulSoup (optional cleanup)
        │
        ▼
Cleaning Pipeline
    ├── Remove HTML boilerplate
    ├── Remove header/footer/nav
    ├── Remove ads/scripts/styles
    ├── Unicode normalization
    ├── Whitespace normalization
    ├── Empty page removal
    ├── Spam removal
    ├── PII removal (spaCy / Presidio / regex)
    ├── Language detection (fastText)
    └── Metadata extraction
        │
        ▼
Deduplication
    ├── URL Canonicalization
    ├── SHA256 (exact duplicates)
    ├── MinHash
    ├── SimHash
    └── LSH (near duplicates)
        │
        ▼
Quality Filtering
    ├── DistilBERT Quality Classifier
    ├── Readability
    ├── Content length
    ├── Spam classifier
    └── Toxicity filter
        │
        ▼
Chunking
        │
        ▼
Storage
    ├── JSONL / Parquet
    ├── DuckDB
    └── Metadata Database
        │
        ▼
Indexing
    ├── BM25
    ├── Embeddings
    └── Hybrid Index
        │
        ▼
Search / RAG / Fine-tuning
```

# Project Workflow

## 0. Domain
- AI
- Programming
- Research Papers
- Official Documentation

## 1. Seed Collection

Correct.

Add: - Sitemap.xml - RSS Feeds - Previously discovered URLs - Common
Crawl (optional)

------------------------------------------------------------------------

## 2. URL Frontier

Should be a **priority queue**, not just a URL list.

Priority can depend on: - Domain authority - Freshness - Topic
relevance - Crawl depth

------------------------------------------------------------------------

## 3. Crawling

Use Crawl4AI:

-   BFSDeepCrawlStrategy
-   BestFirstDeepCrawlStrategy
-   AdaptiveCrawler

Adaptive crawling is useful for domain-specific search because it spends
more effort on high-quality sections.

------------------------------------------------------------------------

## 4. Content Extraction

Primary choice: - Trafilatura

Alternatives: - jusText - Readability

BeautifulSoup is mainly for additional HTML processing.

------------------------------------------------------------------------

## 5. Cleaning

Recommended order:

1.  Extract article
2.  Remove boilerplate
3.  Remove scripts/styles
4.  Unicode normalization
5.  Remove duplicate lines
6.  Normalize whitespace
7.  PII removal
8.  Language detection
9.  Metadata extraction

------------------------------------------------------------------------

## 6. PII Removal

choices: - Microsoft Presidio - spaCy - Regex

------------------------------------------------------------------------

## 7. Language Detection

Use fastText.

Store language in metadata.

------------------------------------------------------------------------

## 8. Metadata

Store:

-   URL
-   Canonical URL
-   Domain
-   Language
-   Crawl Time
-   Depth
-   Title
-   Hash
-   Word Count

------------------------------------------------------------------------

## 9. Deduplication

### Exact

SHA256

### Near

-   MinHash
-   SimHash
-   LSH

------------------------------------------------------------------------

## 10. Canonicalization

Normalize:

-   http vs https
-   trailing slash
-   index.html
-   URL parameters (where appropriate)

before duplicate checking.

------------------------------------------------------------------------

## 11. Quality Classifier

DistilBERT is a good lightweight choice.

Score pages based on:

-   Readability
-   Grammar
-   Information density
-   Spam
-   Topic relevance

Discard low-quality pages.

------------------------------------------------------------------------

## 12. Indexing

For search:

-   BM25
-   Dense embeddings
-   Hybrid search

------------------------------------------------------------------------

## 13. Search Ranking

Combine:

-   BM25
-   Embedding similarity
-   Freshness
-   Authority
-   LLM reranker

------------------------------------------------------------------------

# Suggested Tech Stack

## Crawling

-   Crawl4AI
-   Playwright

## Extraction

-   Trafilatura
-   jusText

## Cleaning

-   BeautifulSoup
-   spaCy
-   fastText

## Deduplication

-   SHA256
-   datasketch (MinHash)
-   LSH

## Storage

-   DuckDB
-   Parquet
-   JSONL

## Embeddings

-   Nomic
-   E5

## Search

-   BM25
-   FAISS / Qdrant / Milvus

## Final Architecture 

``` bash

                      Seed URLs
                           │
                           ▼
                  URL Normalization
                           │
                           ▼
                    URL Frontier
                           │
                           ▼
                    robots.txt Check
                           │
                           ▼
                 Adaptive Scheduler
                           │
                           ▼
                 URL Hash / Visited DB
                           │
                           ▼
                  Crawl4AI Workers
                           │
                           ▼
                    Raw HTML Store
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
     Link Extraction               Trafilatura
            │                             │
            ▼                             ▼
      Link Graph                  Clean Markdown
            │                             │
            └──────────────┬──────────────┘
                           ▼
                 Metadata Extraction
                           │
                           ▼
               FastText Language Detection
                           │
                           ▼
                  PII Detection/Removal
                           │
                           ▼
                  URL Canonicalization
                           │
                           ▼
               SHA-256 Exact Deduplication
                           │
                           ▼
                 MinHash + LSH Near Dedup
                           │
                           ▼
              DistilBERT Quality Classifier
                           │
                           ▼
             Document/Topic Classification
                           │
                           ▼
                     Chunk Generation
                           │
                           ▼
            Chunk Metadata + Document IDs
                           │
                           ▼
                 DuckDB + Parquet Storage
                           │
                           ▼
               Dense Embedding Generation
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
             BM25 Index      Vector Index
                  │                 │
                  └────────┬────────┘
                           ▼
                  Hybrid Retrieval
                           │
                           ▼
                  Cross-Encoder Reranker
                           │
                           ▼
                     LLM Generation
                           │
                           ▼
                    Citation Generator
                           │
                           ▼
                    Final AI Response
```

## Current Project Structure

``` 
NexaSearch/
├── .venv/
├── .env
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── README.md
├── project_timeline.md
│
├── sources/
│   ├── __init__.py
│   └── sources.py
│
├── src/
│   ├── crawler/
│   │   ├── __init__.py
│   │   ├── crawler.py
│   │   ├── adaptive_crawl.py
│   │   └── sitemap.py
│   │
│   ├── cleaner/
│   │   ├── __init__.py
│   │   └── distil_robert.py
│   │
│   ├── pipeline/
│   │   └── __init__.py
│   │
│   └── utils/
│       └── __init__.py
│
├── data/
│   ├── raw/
│   │   ├── json/
│   │   ├── markdown/
│   │   └── sitemap/
│   │       ├── sitemap_data.xml
│   │       └── sitemap_url.xml
│   │
│   ├── processed/
│   └── cleaned/
│
├── tests/
│   ├── test_crawler.py
│   ├── test_sitemap.py
│   ├── test_cleaner.py
│   └── test_sources.py
│
├── docs/
├── scripts/
└── logs/

```

## Future Project Structure
### Note :-  
Project Structure may be vary o short accoding to need.
``` bash

NexaSearch/
├── .venv/
├── .env
├── .env.example
├── .gitignore
├── .dockerignore
├── pyproject.toml
├── requirements.txt
├── Makefile
├── README.md
├── project_timeline.md
│
├── config/
│   ├── __init__.py
│   ├── settings.py              # single source of truth for env vars (pydantic-settings)
│   ├── logging.yaml
│   ├── crawl_config.yaml        # frontier weights, depth limits, domain rules
│   └── model_config.yaml        # embedding model, classifier thresholds, versions
│
├── sources/
│   ├── __init__.py
│   └── sources.py                # seed lists: docs, wikipedia, github, papers, RSS
│
├── src/
│   ├── __init__.py
│   │
│   ├── crawler/
│   │   ├── __init__.py
│   │   ├── crawl4ai_client.py     # BFS / BestFirst / Adaptive strategy wrappers
│   │   ├── sitemap.py             # sitemap.xml / RSS parsing
│   │   ├── robots.py              # robots.txt compliance check
│   │   ├── fetcher.py             # raw HTML fetch + retry/backoff
│   │   └── visited_store.py       # URL hash / seen-before DB
│   │
│   ├── frontier/                  # <- promoted to its own module, not buried in crawler
│   │   ├── __init__.py
│   │   ├── priority_queue.py      # the actual queue implementation
│   │   ├── scoring.py             # domain authority + freshness + topic relevance + depth
│   │   └── scheduler.py           # adaptive scheduling loop, rate limiting per domain
│   │
│   ├── extractor/
│   │   ├── __init__.py
│   │   ├── trafilatura_extractor.py
│   │   ├── justext_extractor.py
│   │   ├── bs4_fallback.py
│   │   └── link_extractor.py      # builds link graph from raw HTML
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── clean.py               # boilerplate/scripts/whitespace/unicode normalize
│   │   ├── pii.py                 # presidio / spacy / regex
│   │   ├── language.py            # fasttext detection
│   │   ├── metadata.py            # title, hash, word count, canonical url, crawl time
│   │   └── dedup/
│   │       ├── __init__.py
│   │       ├── canonicalize.py    # URL canonicalization rules
│   │       ├── exact.py           # SHA-256
│   │       └── near.py            # MinHash + SimHash + LSH
│   │
│   ├── quality/
│   │   ├── __init__.py
│   │   ├── distilbert_classifier.py
│   │   ├── readability.py
│   │   └── toxicity_filter.py
│   │
│   ├── chunking/
│   │   ├── __init__.py
│   │   └── chunker.py
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── duckdb_store.py
│   │   ├── parquet_store.py
│   │   └── jsonl_store.py
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── embedder.py            # Nomic / E5 wrapper
│   │
│   ├── indexing/
│   │   ├── __init__.py
│   │   ├── bm25_index.py
│   │   ├── vector_index.py        # FAISS / Qdrant / Milvus
│   │   └── hybrid_index.py        # merges BM25 + vector scores
│   │
│   ├── search/                    # <- query-time path, separate from indexing (build-time)
│   │   ├── __init__.py
│   │   ├── query.py               # query parsing / cleaning / expansion
│   │   ├── retriever.py           # hits hybrid_index, returns candidates
│   │   ├── reranker.py            # cross-encoder rerank
│   │   └── ranking.py             # blends BM25 + embedding + freshness + authority
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── context_builder.py     # assembles retrieved chunks into a prompt
│   │   ├── generator.py           # LLM call for final answer
│   │   └── citations.py           # maps generated text back to source chunks
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── orchestrator.py        # runs crawl → process → index end-to-end
│   │   ├── stages.py              # stage definitions/registry
│   │   └── state.py               # per-URL/doc status tracking, resume on crash
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py                # FastAPI app entrypoint
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── search.py          # /search endpoint -> src/search
│   │   │   ├── rag.py             # /ask endpoint -> src/rag
│   │   │   └── crawl.py           # trigger/monitor crawl jobs
│   │   ├── schemas.py             # pydantic request/response models
│   │   └── deps.py                # shared dependencies (db conn, index handles)
│   │
│   └── utils/
│       ├── __init__.py
│       ├── io.py
│       ├── logger.py
│       └── hashing.py
│
├── models/                        # gitignored, pulled via script
│   ├── distilbert-quality/
│   ├── fasttext-lang/
│   ├── embeddings/
│   └── registry.json              # tracks model version used per index build
│
├── data/
│   ├── raw/
│   │   ├── html/                  # gzipped, TTL'd — see scripts/gc_raw.py
│   │   ├── json/
│   │   ├── markdown/
│   │   └── sitemap/
│   │       ├── sitemap_data.xml
│   │       └── sitemap_url.xml
│   ├── processed/
│   ├── cleaned/
│   ├── chunks/
│   └── index/
│       ├── bm25/
│       └── vector/
│
├── evals/                         # retrieval + RAG quality tracking
│   ├── queries.jsonl              # labeled query set (start with ~20-50)
│   ├── run_retrieval_eval.py      # precision@k, nDCG
│   └── run_rag_eval.py            # answer relevance / citation accuracy
│
├── notebooks/                     # exploration only, not shipped
│
├── tests/
│   ├── __init__.py
│   ├── fixtures/                  # sample HTML, sitemaps, malformed edge cases
│   ├── unit/
│   │   ├── test_crawler.py
│   │   ├── test_frontier.py
│   │   ├── test_extractor.py
│   │   ├── test_processing.py
│   │   ├── test_quality.py
│   │   ├── test_chunking.py
│   │   ├── test_storage.py
│   │   ├── test_indexing.py
│   │   ├── test_search.py
│   │   └── test_sources.py
│   └── integration/
│       ├── test_crawl_pipeline.py
│       └── test_search_end_to_end.py
│
├── scripts/
│   ├── run_pipeline.py
│   ├── crawl.sh
│   ├── build_index.sh
│   ├── download_models.py
│   └── gc_raw.py                  # cleans up raw HTML after successful processing
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docs/
│   ├── architecture.md
│   └── api.md
│
└── logs/
```

## Duplicate selection pipeline

``` bash
                Crawl Page
                     │
                     ▼
          Extract Main Content
                     │
         Normalize & Canonicalize
                     │
                     ▼
               SHA-256 Check
             (Exact Duplicate)
                     │
             Duplicate? Skip
                     │
                     ▼
        Create Shingles (2/3/5-grams)
                     │
                     ▼
             MinHash Signature
                     │
                     ▼
             Split into Bands
                     │
                     ▼
             LSH Bucketing
                     │
                     ▼
          Candidate Documents
                     │
                     ▼
      Exact Jaccard Similarity
                     │
        Near Duplicate?
            │             │
          Yes           No
          Skip         Index
```

## Inverted Index (Two Parts)
``` bash
Dictionary

python
java
awesome
fast
is
      │
      ▼
-------------------------
Posting Lists

python  → [1,3]

java    → [2]

awesome → [1,2]

fast    → [3]

is      → [1,2,3]

```
### Complete Posting list 
After Term Frequency, Document Frequency (NO. OF DOCUMENT CONTAIN A WORD )and Positional Index 

#### POSTING index will be :-
``` bash

python

↓

Doc1

TF = 5

Positions = (3, 18, 27, 40, 52)

Field = Title
```

## With BM25 (USE ELASTIC SEARCH)

``` bash
User Query
      │
      ▼
Tokenizer
      │
      ▼
Dictionary Lookup
      │
      ▼
Posting Lists
      │
      ▼
BM25 Score            
      │
      ▼
Sort by Score
      │
      ▼
Top Results
```

## Query Processing 

``` bash
User Query
      │
      ▼
Tokenize
      │
      ▼
Normalize
      │
      ▼
Dictionary Lookup
      │
      ▼
Posting Lists
      │
      ▼
Boolean Operations
      │
      ▼
Candidate Documents
      │
      ▼
BM25
      │
      ▼
Top 100 Results
```

``` bash

| Query Type      | Operation                     |
| --------------- | ----------------------------- |
| AND             | Intersection of posting lists |
| OR              | Union of posting lists        |
| NOT             | Difference of posting lists   |
| Phrase          | Position check                |
| Wildcard        | Pattern matching              |
| Prefix          | Trie/autocomplete             |
| Fuzzy           | Edit distance                 |
| Query Expansion | Add related terms             |

```

## Index Compressiona nd Skip list 
use Lucene 

``` bash
Crawler
      │
      ▼
Tokenizer
      │
      ▼
Inverted Index
      │
      ▼
Posting Lists
      │
      ▼
Compression
      │
      ▼
Skip Lists
      │
      ▼
Stored on Disk
      │
      ▼
Query Engine
      │
      ▼
BM25
```

## Sharding

``` bash
                Web Crawl

                    │

                    ▼

             Document Parser

                    │

                    ▼

             Assign to Shard

        ┌──────────┼──────────┐

        ▼          ▼          ▼

     Shard1     Shard2     Shard3

        │          │          │

        ▼          ▼          ▼

     Segment     Segment    Segment

        │          │          │

        └──────Merge──────────┘

                    │

                    ▼

             Distributed Search
```

## Query Document Ranking

``` bash
User Query
      │
      ▼
Query Understanding
      │
      ▼
─────────────────────────────
Parallel Retrieval
─────────────────────────────

BM25

↓

200 Docs

Vector Search

↓

200 Docs

Metadata Filter

↓

50 Docs

─────────────────────────────
Merge
─────────────────────────────

↓

300 Candidates

↓

Cross Encoder

↓

Top 20

↓

LLM

↓

Answer
```

## Reranker
``` 
                 Query
                   │
        ┌──────────┴──────────┐
        │                     │
     BM25                 Vector Search
    Top-200                 Top-200
        │                     │
        └──────────┬──────────┘
                   │
             Remove Duplicates
                   │
                 RRF Fusion
                   │
            ~250–320 candidates
                   │
              Cross-Encoder
                 Reranker
                   │
                Top-20
                   │
           Answer Generation / UI
```
## Using Cross Encoder
``` bash
BM25

↓

200 Docs

----------------

Vector Search

↓

200 Docs

----------------

Merge

↓

300 Docs

----------------

Cross Encoder

↓

Top 20
```

## Cross Encoder pipeline
``` bash
                User Query
                     │
                     ▼
             Query Understanding
                     │
       ┌─────────────┴─────────────┐
       ▼                           ▼
    BM25                    Vector Search
       │                           │
       ▼                           ▼
   Top 100 Docs              Top 100 Docs
       └─────────────┬─────────────┘
                     ▼
               Merge Results
                     ▼
           Cross Encoder Reranker
                     ▼
                Top 20 Chunks
                     ▼
                     LLM
                     ▼
                  Final Answer

```

## RRF

``` bash
GitHub
Documentation
Stack Overflow
Research Papers
        │
        ▼
Crawler & Parser
        │
        ▼
Chunk Documents
        │
   ┌────┴────┐
   ▼         ▼
BM25      Embeddings
   │         │
   ▼         ▼
Top100   Top100
     └────┬────┘
          ▼
         RRF
          ▼
Cross Encoder
          ▼
Top20 Chunks
          ▼
LLM
          ▼
Final Answer
```