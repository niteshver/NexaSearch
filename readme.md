# NexaSearch 

An open-source vertical search engine for developers, researchers, and AI practitioners.

> We don't compete in data. We compete in depth.

## Demo
--------->COMING<---------

## Why Nexasearch?

Google is excellent for general web search.

But developers often need to search:

• GitHub Issues
• Pull Requests
• Documentation
• Research Papers
• PDFs
• API References

NexaSearch brings these sources together into one search experience.

## Features

- Hybrid Search (BM25 + Vector)

- Research Paper Search

- GitHub Search

- Documentation Search

- PDF Search

- Live Crawling

- Semantic Retrieval

- Cross Encoder Reranking

- Open Source

## Language & Technology Used

- Python
- CSS/JS
- Crawler
- RAG

## Project Structure

``` text
NexaSearch/
├── .env.example
├── .gitignore
├── app_streamlit.py
├── cli.py
├── pyproject.toml
├── readme.md
├── uv.lock
├── cleaner/
│   └── distil_robert.py
├── data/
│   ├── index/
│   ├── nexasearch.db
│   └── raw/
│       ├── json/
│       ├── markdown/
│       ├── pdf/
│       └── sitemap/
├── doc/
├── evals/
│   └── evaluator.py
├── sources/
│   └── sources.py
├── src/
│   ├── Indexing/
│   │   ├── ranking.py
│   │   └── vector_index.py
│   ├── chunking/
│   │   └── chunker.py
│   ├── config/
│   │   └── settings.py
│   ├── crawler/
│   │   ├── crawler.py
│   │   ├── robots.py
│   │   └── sitemap.py
│   ├── embedding/
│   │   └── embedder.py
│   ├── pipeline/
│   │   └── orchestrator.py
│   ├── processing/
│   │   ├── cleaner.py
│   │   └── deduplication.py
│   ├── quality/
│   │   └── quality_filter.py
│   ├── search/
│   │   └── engine.py
│   ├── seeder/
│   │   └── url_seeder.py
│   └── storage/
│       └── duckdb_store.py
└── tests/
    ├── test_chunker.py
    ├── test_cleaner.py
    ├── test_deduplication.py
    ├── test_indexing.py
    ├── test_lsh.py
    └── test_quality.py
```

## Workflow
``` text
Seed Sources
      │
      ▼
 Crawl Pipeline
      │
      ▼
 Data Processing
      │
      ▼
 Hybrid Index
      │
      ▼
 Search
      │
      ▼
   Top 50
      |
 AI Answer (Optional)

```
-> For the complete system design follow docs/architecture.md

## Installation

### 1. Fork the Repository

Fork this repository to your GitHub account by clicking the **Fork** button.

### 2. Clone the Repository

Clone your fork to your local machine.

```bash
git clone https://github.com/<niteshver>/NexaSearch.git
```

### 3. Navigate to the Project Directory

```bash
cd NexaSearch
```

### 4. Create a Virtual Environment

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 5. Install Dependencies

using **uv**:

```bash
uv sync
```

### 6. Configure Environment Variables

Create a `.env` file in the project root and add the required configuration.

```env
# Example
OPENAI_API_KEY=your_api_key
```

### 7. Run the Project

```bash
example
```

