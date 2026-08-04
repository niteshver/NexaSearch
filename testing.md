Crawler
      │
      ▼
Raw HTML
      │
      ▼
Content Extraction
      │
      ▼
Boilerplate Removal
      │
      ▼
Text Cleaning
      │
      ▼
Metadata Extraction
      │
      ▼
Language Detection
      │
      ▼
URL Canonicalization
      │
      ▼
Duplicate Detection
      │
      ▼
Quality Scoring
      │
      ▼
Chunking
      │
      ▼
JSON / Parquet
      │
      ▼
Indexing


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

## Vertical search Enigne

``` bash
Raw HTML
      │
      ▼
Encoding Detection
      │
      ▼
Content Extraction
      │
      ▼
HTML Cleaning
      │
      ▼
Metadata Extraction
      │
      ▼
Language Detection
      │
      ▼
Canonicalization
      │
      ▼
Duplicate Detection
      │
      ▼
Quality Filtering
      │
      ▼
Tokenization
      │
      ▼
Normalization
      │
      ▼
Chunking
      │
      ▼
CleanDocument
```

