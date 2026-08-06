#!/usr/bin/env python3
"""
Enterprise-Scale URL Seeder CLI - Discover 2M+ URLs

Usage:
  python seed_enterprise.py                    # Seed top 30 sources
  python seed_enterprise.py --all-sources      # All sources (2M+)
  python seed_enterprise.py --mega-only        # Only 100K+ sources
  python seed_enterprise.py --source arxiv.org # Specific source
"""

import asyncio
import sys
import argparse
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

from src.seeder.enterprise_url_seeder import EnterpriseURLSeeder
from src.seeder.enterprise_sources import (
    ALL_ENTERPRISE_SOURCES,
    get_top_sources,
    get_mega_sources,
    calculate_total_estimated_urls,
)


async def run_seeding(
    all_sources: bool = False,
    mega_only: bool = False,
    top_n: int = 30,
    specific_sources: list = None,
) -> int:
    """Run enterprise-scale URL seeding."""
    
    seeder = EnterpriseURLSeeder()
    
    # Determine sources
    if all_sources:
        source_list = None  # Will use all
        tier_mode = "all"
        logger.info(f"🚀 Seeding ALL {len(ALL_ENTERPRISE_SOURCES)} sources (2M+ URLs)")
    elif mega_only:
        mega = get_mega_sources()
        source_list = list(mega.keys())
        tier_mode = "mega"
        logger.info(f"🚀 Seeding {len(mega)} mega sources (100K+ URLs each)")
    elif specific_sources:
        source_list = specific_sources
        tier_mode = "custom"
        logger.info(f"🚀 Seeding {len(source_list)} specific sources")
    else:
        source_list = None
        tier_mode = "top30"
        logger.info(f"🚀 Seeding top {top_n} priority sources")
    
    logger.info(f"📊 Estimated total URLs: {calculate_total_estimated_urls():,}\n")
    
    try:
        result = await seeder.seed_urls(
            source_domains=source_list,
            tier_mode=tier_mode,
        )
        
        # Generate master_seed.xml
        logger.info("\n📝 Generating master_seed.xml (use this for crawling)...")
        seeder.save_master_sitemap_xml("master_seed.xml")
        
        # Generate seeds.json
        logger.info("📝 Generating seeds.json (complete index)...")
        seeder.save_comprehensive_json("seeds.json")
        
        logger.info("\n" + "="*90)
        logger.info("✓ ENTERPRISE SEEDING COMPLETE")
        logger.info("="*90)
        logger.info(f"Total URLs discovered: {result['total_urls']:,}")
        logger.info(f"Sources succeeded: {result['sources_succeeded']}")
        logger.info(f"Sources failed: {result['sources_failed']}")
        logger.info(f"Time elapsed: {result['elapsed_seconds']:.1f}s ({result['elapsed_seconds']/60:.1f} minutes)")
        logger.info(f"\n📁 Output files:")
        logger.info(f"   1. data/raw/sitemap/master_seed.xml (FOR CRAWLING)")
        logger.info(f"   2. data/raw/sitemap/seeds.json (Complete index)")
        logger.info("="*90 + "\n")
        
        return 0
        
    except KeyboardInterrupt:
        logger.info("\n✗ Interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"\n✗ Error: {e}", exc_info=True)
        return 1


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Enterprise-Scale URL Seeder - Discover 2M+ URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Seed top 30 sources (default, fast)
  python seed_enterprise.py
  
  # Seed all sources (2M+ URLs, comprehensive)
  python seed_enterprise.py --all-sources
  
  # Seed only mega sources (100K+ each)
  python seed_enterprise.py --mega-only
  
  # Seed specific sources
  python seed_enterprise.py --source arxiv.org --source pytorch.org
  
  # Custom top N sources
  python seed_enterprise.py --top-n 50

Output:
  master_seed.xml  ← Use this for crawling
  seeds.json       ← Complete index with metadata
        """
    )
    
    parser.add_argument(
        "--all-sources",
        action="store_true",
        help="Seed all sources (2M+ URLs, takes 2-4 hours)"
    )
    
    parser.add_argument(
        "--mega-only",
        action="store_true",
        help="Seed only mega sources (100K+ URLs each)"
    )
    
    parser.add_argument(
        "--top-n",
        type=int,
        default=30,
        help="Seed top N sources by priority (default: 30)"
    )
    
    parser.add_argument(
        "--source",
        action="append",
        help="Specific source to seed (can use multiple times)"
    )
    
    parser.add_argument(
        "--list-sources",
        action="store_true",
        help="List all available sources and exit"
    )
    
    args = parser.parse_args()
    
    # List sources if requested
    if args.list_sources:
        logger.info(f"\nAvailable sources ({len(ALL_ENTERPRISE_SOURCES)} total):\n")
        for i, (domain, config) in enumerate(sorted(ALL_ENTERPRISE_SOURCES.items()), 1):
            logger.info(f"{i:3d}. {domain:40} | Type: {config['source_type']:15} | Est: {config['urls_estimate']:>8,}")
        logger.info("")
        return 0
    
    # Validate specific sources
    if args.source:
        invalid = [s for s in args.source if s not in ALL_ENTERPRISE_SOURCES]
        if invalid:
            logger.error(f"Unknown sources: {invalid}")
            logger.info(f"Use --list-sources to see available sources")
            return 1
    
    return asyncio.run(
        run_seeding(
            all_sources=args.all_sources,
            mega_only=args.mega_only,
            top_n=args.top_n,
            specific_sources=args.source,
        )
    )


if __name__ == "__main__":
    sys.exit(main())
