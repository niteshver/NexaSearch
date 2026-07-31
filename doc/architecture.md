# Architecture
We follow simiar architecture for NexaSearch as followed by Google Search Engine and other search engine.


## Data Collection Pipeline

```text
                                    Seed Sources
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        │                                │                                │
        ▼                                ▼                                ▼
 Official Documentation            GitHub Repositories          Research Papers
        │                                │                                │
        ├───────────────┬────────────────┴────────────────┬───────────────┤
        ▼               ▼                                 ▼
   Technical Blogs   News / RSS Feeds              XML Sitemaps
                                         │
                                         ▼
                               URL Discovery Service
                                         │
                     ┌───────────────────┴───────────────────┐
                     │                                       │
                     ▼                                       ▼
              URL Canonicalization                  robots.txt Validation
                     │                                       │
                     └───────────────────┬───────────────────┘
                                         ▼
                             URL Frontier (Priority Queue)
                                         │
                                         ▼
                              Crawl Scheduler
                  (Adaptive / BFS / Best-First Strategy)
                                         │
                                         ▼
                               Crawl4AI Workers
                                         │
                                         ▼
                               Raw HTML Collection
                                         │
                                         ▼
                           Main Content Extraction
                     ┌────────────┬────────────┬────────────┐
                     │            │            │
                     ▼            ▼            ▼
                 Trafilatura   jusText     BeautifulSoup
                                         │
                                         ▼
                             Content Processing Pipeline
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        │                                │                                │
        ▼                                ▼                                ▼
 Boilerplate Removal          Metadata Extraction            Language Detection
 Header/Footer Removal         URL, Title, Author            fastText
 Script & Style Removal        Published Date
 Unicode Normalization         Crawl Timestamp
 Whitespace Cleanup
 PII Removal
 Spam Removal
                                         │
                                         ▼
                              Duplicate Detection
                     ┌────────────┬────────────┬────────────┐
                     │            │            │
                     ▼            ▼            ▼
             URL Canonicalization   SHA-256   MinHash + SimHash + LSH
                                         │
                                         ▼
                              Quality Assessment
                     ┌────────────┬────────────┬────────────┐
                     │            │            │
                     ▼            ▼            ▼
             Content Quality   Readability   Spam / Toxicity
                                         │
                                         ▼
                                 Document Chunking
                                         │
                                         ▼
                              Persistent Storage
                     ┌────────────┬────────────┬────────────┐
                     │            │            │
                     ▼            ▼            ▼
                  JSONL        Parquet       DuckDB
                                         │
                                         ▼
                                Indexing Pipeline
```

## Indexing Pipeline

The Indexing Pipeline transforms processed documents into optimized search indexes that support fast and accurate retrieval. NexaSearch combines lexical search (BM25) with semantic vector search to provide a hybrid retrieval system.

1. Document Preparation

Before indexing, every document is normalized and enriched with metadata.

### Processing includes:
- Tokenization
- Text normalization
- Metadata association
- Chunk generation

Each chunk becomes an independent searchable unit while retaining a reference to its parent document.

-> Output: Search-ready document chunks.

2. Lexical Index (BM25)

The lexical index enables keyword-based retrieval using an inverted index. During indexing, each token is mapped to the documents in which it appears, along with statistics such as term frequency and token positions.

``` text

Document Chunks
       │
       ▼
 Tokenization
       │
       ▼
 Inverted Index
       │
       ▼
 Posting Lists
       │
       ▼
 BM25 Index

```
### Each posting entry stores:

- Document ID
- Term Frequency (TF)
- Document Frequency (DF)
- Token Positions
- Field Information (Title, Body, etc.)

This structure enables efficient keyword lookup and phrase queries.

3. Vector Index

Each document chunk is converted into a dense embedding using an embedding model. These embeddings are stored in a vector database to support semantic similarity search.

``` text
Document Chunks
       │
       ▼
Embedding Model
       │
       ▼
Embedding Vectors
       │
       ▼
Vector Index
```
Unlike BM25, vector search retrieves documents based on semantic meaning rather than exact keyword matches.

4. Hybrid Index

NexaSearch combines lexical and semantic indexes to improve retrieval quality.

``` text
                Document Chunks
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     BM25 Index             Vector Index
          │                       │
          └───────────┬───────────┘
                      ▼
               Hybrid Retrieval
```

Hybrid retrieval improves recall by combining exact keyword matching with semantic similarity.

## Retrieval Pipeline

Both lexical and semantic retrieval are executed in parallel.
``` text
                 User Query
                      │
                      ▼
             Query Processing
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
      BM25                    Vector Search
   Top 100 Results          Top 100 Results
        └─────────────┬─────────────┘
                      ▼
               Reciprocal Rank Fusion
                      ▼
              Candidate Documents

```
Reciprocal Rank Fusion (RRF) merges results from both retrieval methods into a single ranked candidate list.

## Reranking

The merged candidates are reranked using a Cross-Encoder model.

``` text
Candidate Documents
        │
        ▼
Cross-Encoder
        │
        ▼
 Top 20 Results
```
Unlike vector similarity, the Cross-Encoder evaluates the query-document pair together, producing more accurate relevance scores.

## Final Retrieval Pipeline

``` text
User Query
      │
      ▼
Query Processing
      │
      ▼
──────────────────────────────────
Parallel Retrieval
──────────────────────────────────
      │
 ┌────┴─────┐
 ▼          ▼
BM25     Vector Search
 │            │
 └────┬───────┘
      ▼
 Recipocal Rank Fusion (RRF)
      │
      ▼
Cross-Encoder Reranker
      │
      ▼
Top Ranked Chunks
      │
      ▼
LLM
      │
      ▼
Final Answer
```


