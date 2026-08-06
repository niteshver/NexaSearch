#!/usr/bin/env python3
"""
Production CLI for AI/ML Vertical Search Engine - URL Seeding

Usage:
  python seed_ai_ml.py                      # Seed top 20 sources
  python seed_ai_ml.py --all-sources        # Seed all 80+ sources
  python seed_ai_ml.py --source arxiv.org   # Seed specific source
  python seed_ai_ml.py --limit-per-source 5000  # Custom limit
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
logger = logging.getLogger(__name__)

from src.seeder.ai_ml_url_seeder import AIMLURLSeeder
from src.seeder.ai_ml_sources import ALL_SOURCES, get_top_sources


async def run_seeding(
    all_sources: bool = False,
    specific_sources: list = None,
    limit_per_source: int = 10000,
) -> int:
    """Run URL seeding."""
    
    seeder = AIMLURLSeeder()
    
    # Determine sources
    if all_sources:
        source_list = list(ALL_SOURCES.keys())
        logger.info(f"Seeding ALL {len(source_list)} sources...")
    elif specific_sources:
        source_list = specific_sources
        logger.info(f"Seeding {len(source_list)} specific sources...")
    else:
        source_list = None  # Will use top 20
        logger.info(f"Seeding top 20 priority sources...")
    
    try:
        result = await seeder.seed_urls(
            source_domains=source_list,
            limit_urls_per_source=limit_per_source,
        )
        
        # Save outputs
        seeder.save_json_seeds("ai_ml_seeds.json")
        seeder.generate_sitemap_xml("ai_ml_sitemap.xml")
        
        logger.info("\n" + "="*80)
        logger.info("✓ SEEDING COMPLETE")
        logger.info("="*80)
        logger.info(f"Total URLs: {result['total_urls']}")
        logger.info(f"Sources succeeded: {result['sources_succeeded']}")
        logger.info(f"Sources failed: {result['sources_failed']}")
        logger.info(f"\nOutput files:")
        logger.info(f"  • Seeds JSON: ./data/raw/sitemap/ai_ml_seeds.json")
        logger.info(f"  • Sitemap XML: ./data/raw/sitemap/ai_ml_sitemap.xml")
        logger.info("="*80 + "\n")
        
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
        description="AI/ML Vertical Search Engine - URL Seeder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Seed top 20 sources
  python seed_ai_ml.py
  
  # Seed all 80+ sources
  python seed_ai_ml.py --all-sources
  
  # Seed specific sources
  python seed_ai_ml.py --source arxiv.org --source pytorch.org
  
  # Custom limit per source
  python seed_ai_ml.py --limit-per-source 5000
        """
    )
    
    parser.add_argument(
        "--all-sources",
        action="store_true",
        help="Seed all 80+ AI/ML sources (default: top 20)"
    )
    
    parser.add_argument(
        "--source",
        action="append",
        help="Specific source to seed (can use multiple times)"
    )
    
    parser.add_argument(
        "--limit-per-source",
        type=int,
        default=10000,
        help="Max URLs per source (default: 10000)"
    )
    
    args = parser.parse_args()
    
    # Validate specific sources
    if args.source:
        invalid = [s for s in args.source if s not in ALL_SOURCES]
        if invalid:
            logger.error(f"Unknown sources: {invalid}")
            logger.info(f"Available sources: {list(ALL_SOURCES.keys())}")
            return 1
    
    return asyncio.run(
        run_seeding(
            all_sources=args.all_sources,
            specific_sources=args.source,
            limit_per_source=args.limit_per_source,
        )
    )


if __name__ == "__main__":
    sys.exit(main())
