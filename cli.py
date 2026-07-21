import argparse
import asyncio
import os
import sys
from pathlib import Path

# Add root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.pipeline.orchestrator import NexaSearchPipeline
from src.crawler.logger import logger
from evals.evaluator import EvaluationSet, QueryEvaluation

def run_crawl(args):
    urls = []
    if args.urls:
        urls = [u.strip() for u in args.urls.split(",") if u.strip()]
    elif args.file:
        path = Path(args.file)
        if path.exists():
            with open(path, "r") as f:
                urls = [line.strip() for line in f if line.strip()]
        else:
            logger.error(f"File not found: {args.file}")
            sys.exit(1)

    if not urls:
        logger.error("No URLs provided to crawl.")
        sys.exit(1)

    pipeline = NexaSearchPipeline()
    # Override settings temporarily if specified
    if args.max_pages:
        pipeline.crawler.max_pages = args.max_pages
    if args.max_depth:
        pipeline.crawler.max_depth = args.max_depth

    logger.info(f"Running crawl pipeline for {len(urls)} URLs...")
    stats = asyncio.run(pipeline.run(urls))
    print("\nPipeline Execution Summary:")
    print("=" * 40)
    print(f"Status: {stats.get('status')}")
    print(f"Total time: {stats.get('total_time_seconds')} seconds")
    for stage, info in stats.get("stages", {}).items():
        print(f" - Stage '{stage}': {info.get('time_seconds')}s")
    print("=" * 40)

def run_search(args):
    pipeline = NexaSearchPipeline()
    logger.info(f"Searching for query: '{args.query}'")
    results = pipeline.search(
        args.query,
        top_k=args.top_k,
        use_vector=not args.no_vector,
        use_rerank=not args.no_rerank
    )
    
    if not results:
        print("\nNo matching results found. Build the search index first.")
        return

    print(f"\nFound {len(results)} results:")
    print("=" * 80)
    for r in results:
        print(f"{r['rank']}. {r['title']} (Score: {r['score']})")
        print(f"   URL: {r['url']}")
        print(f"   Heading: {r['heading']} | Quality Score: {r['quality_score']}")
        print(f"   Snippet: {r['snippet']}")
        print("-" * 80)

def run_eval(args):
    logger.info("Running search evaluation set...")
    pipeline = NexaSearchPipeline()
    
    # Check if index has documents
    db_stats = pipeline.get_stats()
    if db_stats["document_count"] == 0:
        logger.error("Database is empty. Please run a crawl to index pages before running evaluations.")
        sys.exit(1)

    # 1. Define a set of evaluation queries based on standard crawled content
    # We will look for some URLs in the DB to form a mock evaluation set
    chunks = pipeline.store.get_all_chunks()
    if not chunks:
        logger.error("No indexed chunks found to evaluate.")
        sys.exit(1)
        
    eval_set = EvaluationSet()
    
    # Formulate 3-5 query validations dynamically from our chunks
    queries_to_eval = []
    # Query 1: search words from a random title
    for c in chunks[:3]:
        words = c["title"].split()
        if len(words) >= 2:
            query = " ".join(words[:3])
            # The relevant target is the document URL
            queries_to_eval.append((query, c["url"]))
            
    if not queries_to_eval:
        queries_to_eval = [
            ("python documentation", chunks[0]["url"]),
            ("machine learning", chunks[0]["url"])
        ]

    for idx, (query, relevant_url) in enumerate(queries_to_eval):
        q_eval = QueryEvaluation(query, f"q_{idx+1}", [relevant_url])
        
        # Search using engine
        search_results = pipeline.search(query, top_k=10)
        retrieved_urls = [r["url"] for r in search_results]
        
        q_eval.set_retrieved(retrieved_urls)
        q_eval.evaluate()
        eval_set.add_query(q_eval)
        
    mean_metrics = eval_set.get_mean_metrics()
    print("\nMean Evaluation Metrics:")
    print("=" * 40)
    for metric, score in mean_metrics.items():
        print(f" - {metric}: {score}")
    print("=" * 40)

    # Plot metrics
    chart_path = "evals/eval_results.png"
    json_path = "evals/eval_results.json"
    eval_set.plot_metrics(chart_path)
    eval_set.save_json(json_path)
    logger.info(f"Saved evaluation plots to: {chart_path}")
    logger.info(f"Saved evaluation metrics to: {json_path}")

def run_ui(args):
    logger.info("Launching Streamlit UI...")
    os.system("streamlit run app_streamlit.py")

def main():
    parser = argparse.ArgumentParser(
        description="NexaSearch CLI - Lightweight Domain Search Engine"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Crawl Subcommand
    crawl_parser = subparsers.add_parser("crawl", help="Crawl and index target URLs")
    crawl_parser.add_argument("--urls", type=str, help="Comma-separated list of seed URLs")
    crawl_parser.add_argument("--file", type=str, help="Path to text file containing seed URLs (one per line)")
    crawl_parser.add_argument("--max-pages", type=int, help="Override maximum pages limits")
    crawl_parser.add_argument("--max-depth", type=int, help="Override maximum crawl depth")

    # Search Subcommand
    search_parser = subparsers.add_parser("search", help="Execute search queries")
    search_parser.add_argument("query", type=str, help="Search query string")
    search_parser.add_argument("--top-k", type=int, default=10, help="Number of results to retrieve")
    search_parser.add_argument("--no-vector", action="store_true", help="Disable vector semantic search (BM25 only)")
    search_parser.add_argument("--no-rerank", action="store_true", help="Disable Cross-Encoder reranking")

    # Eval Subcommand
    subparsers.add_parser("eval", help="Run automated evaluation sets and output Seaborn metrics")

    # UI Subcommand
    subparsers.add_parser("ui", help="Launch the Streamlit dashboard")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "crawl":
        run_crawl(args)
    elif args.command == "search":
        run_search(args)
    elif args.command == "eval":
        run_eval(args)
    elif args.command == "ui":
        run_ui(args)

if __name__ == "__main__":
    main()
