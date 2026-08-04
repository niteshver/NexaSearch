#!/usr/bin/env python3
"""
Quick-start script for NexaSearch vertical search engine.

Usage:
  python run_seeder.py              # Run URL seeding only
  python run_seeder.py --resume     # Resume from checkpoint
  python run_seeder.py --clean      # Clear checkpoint and restart
"""

import asyncio
import sys
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from src.seeder.url_seeder import URLSeeder, URLSeederConfig
from src.seeder.sources import SOURCES


async def run_seeding(
    clean: bool = False,
    high_throughput: bool = False,
) -> None:
    """Run URL seeding pipeline."""
    
    output_dir = Path("./data/raw/sitemap")
    checkpoint_file = output_dir / ".seeder_checkpoint.json"
    
    # Clean checkpoint if requested
    if clean and checkpoint_file.exists():
        checkpoint_file.unlink()
        print("✓ Checkpoint cleared")
    
    # Configure seeder
    if high_throughput:
        config = URLSeederConfig(
            output_dir=str(output_dir),
            rate_limit_per_domain=0.2,
            max_retries=3,
            incremental_mode=True,
            batch_size=5,
            parallel_batches=True,
            request_timeout=30.0,
            max_concurrent_per_domain=10,
            stream_to_disk=True,
        )
    else:
        config = URLSeederConfig(
            output_dir=str(output_dir),
            rate_limit_per_domain=1.0,
            max_retries=3,
            incremental_mode=True,
            batch_size=3,
            parallel_batches=True,
            request_timeout=30.0,
            max_concurrent_per_domain=5,
            stream_to_disk=True,
        )
    
    # Create seeder
    seeder = URLSeeder(
        source_domains=list(SOURCES.keys()),
        config=config
    )
    
    # Run discovery
    print(f"\n{'='*80}")
    print(f"[SEEDING] Starting URL discovery")
    print(f"{'='*80}")
    print(f"Config:")
    print(f"  Output: {output_dir}")
    print(f"  Sources: {len(SOURCES)}")
    print(f"  High throughput: {high_throughput}")
    print(f"  Max concurrent: {config.max_concurrent_per_domain}")
    print(f"  Parallel batches: {config.parallel_batches}")
    print(f"  Stream to disk: {config.stream_to_disk}")
    print(f"{'='*80}\n")
    
    try:
        discovered = await seeder.discover_urls(use_bm25_scoring=False)
        
        # Save results
        seeder.save_to_json("seeds.json")
        seeder.generate_sitemap_xml("master_seed.xml")
        
        print(f"\n{'='*80}")
        print(f"✓ SEEDING COMPLETE")
        print(f"{'='*80}")
        print(f"Total URLs: {len(seeder.all_urls)}")
        print(f"Domains succeeded: {len(discovered)}/{len(SOURCES)}")
        print(f"Domains failed: {len(seeder.failed_domains)}")
        print(f"\nOutput files:")
        print(f"  Sitemap: {output_dir}/master_seed.xml")
        print(f"  Seeds JSON: {output_dir}/seeds.json")
        print(f"  Stream JSONL: {output_dir}/seeds_stream.jsonl")
        print(f"{'='*80}\n")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n✗ Interrupted by user")
        return 1
    except Exception as e:
        print(f"\n\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


async def run_crawling() -> None:
    """Run content crawling pipeline."""
    from src.crawler.crawler import CrawlerManager
    import xml.etree.ElementTree as ET
    
    sitemap_path = Path("./data/raw/sitemap/master_seed.xml")
    
    if not sitemap_path.exists():
        print(f"✗ Sitemap not found: {sitemap_path}")
        print("✓ Run seeding first with: python run_seeder.py")
        return 1
    
    # Parse sitemap
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls = []
    for loc in root.findall(".//{*}loc"):
        if loc.text:
            urls.append(loc.text.strip())
    
    print(f"\n{'='*80}")
    print(f"[CRAWLING] Starting content crawling")
    print(f"{'='*80}")
    print(f"URLs to crawl: {len(urls)}")
    print(f"Limiting to: 1000 (demo)")
    print(f"{'='*80}\n")
    
    manager = CrawlerManager()
    
    try:
        crawled = await manager.crawl(urls[:1000])
        
        print(f"\n{'='*80}")
        print(f"✓ CRAWLING COMPLETE")
        print(f"{'='*80}")
        print(f"Documents crawled: {len(crawled)}")
        print(f"Output:")
        print(f"  Markdown: ./data/raw/markdown/")
        print(f"  JSON: ./data/raw/json/")
        print(f"  PDFs: ./data/raw/pdf/")
        print(f"{'='*80}\n")
        
        return 0
        
    except Exception as e:
        print(f"\n\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="NexaSearch Vertical Search Engine - Quick Start"
    )
    parser.add_argument(
        "--stage",
        choices=["seeding", "crawling", "pipeline"],
        default="seeding",
        help="Pipeline stage to run"
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from checkpoint"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clear checkpoint and restart"
    )
    parser.add_argument(
        "--high-throughput",
        action="store_true",
        help="Use high-throughput settings"
    )
    
    args = parser.parse_args()
    
    if args.stage == "seeding":
        return asyncio.run(
            run_seeding(clean=args.clean, high_throughput=args.high_throughput)
        )
    elif args.stage == "crawling":
        return asyncio.run(run_crawling())
    else:
        print("Pipeline stage not yet implemented")
        return 1


if __name__ == "__main__":
    sys.exit(main())
