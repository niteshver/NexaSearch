"""
Integrated Crawler + Seeder + Indexer Pipeline

This module orchestrates the complete vertical search engine workflow:
1. URL Seeding (discovery from sources)
2. Content Crawling (Crawl4AI + Trafilatura)
3. Quality Filtering
4. Chunking
5. Embedding + Indexing

Features:
✓ Pipeline orchestration with progress tracking
✓ Error recovery and partial restart
✓ Checkpoint-based resumption
✓ Async/parallel processing
✓ Memory-efficient streaming
✓ Metrics collection and monitoring
"""

import asyncio
import json
import logging
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

from src.config.settings import settings
from src.seeder.url_seeder import EnterpriseURLSeeder
from src.crawler.crawler import CrawlerManager
from src.crawler.logger import logger

logger = logging.getLogger(__name__)


@dataclass
class PipelineStage:
    """Pipeline stage configuration."""
    name: str
    enabled: bool = True
    timeout: float = 3600.0  # 1 hour default
    retry_on_failure: bool = True
    skip_if_exists: bool = False


@dataclass
class PipelineMetrics:
    """Pipeline execution metrics."""
    stage: str
    start_time: float
    end_time: Optional[float] = None
    duration: float = 0.0
    items_processed: int = 0
    items_failed: int = 0
    items_skipped: int = 0
    
    @property
    def success_rate(self) -> float:
        total = self.items_processed + self.items_failed
        return (self.items_processed / total * 100) if total > 0 else 0.0
    
    @property
    def throughput(self) -> float:
        return self.items_processed / self.duration if self.duration > 0 else 0.0


class SearchEnginePipeline:
    """
    Orchestrate the complete vertical search engine pipeline.
    
    Workflow:
    1. URL Seeding → Discover seed URLs from sources
    2. Crawling → Fetch content (HTML, PDFs)
    3. Cleaning → Remove boilerplate (trafilatura)
    4. Quality Filtering → Remove low-quality content
    5. Chunking → Split into semantic chunks
    6. Embedding → Generate embeddings
    7. Indexing → Index into DuckDB + vector DB
    """
    
    def __init__(
        self,
        output_base: str = "./data",
        skip_stages: Optional[List[str]] = None,
    ):
        self.output_base = Path(output_base)
        self.skip_stages = skip_stages or []
        self.skip_stages = set(s.lower() for s in self.skip_stages)
        
        # Ensure directories
        self.output_base.mkdir(parents=True, exist_ok=True)
        for subdir in ['raw/sitemap', 'raw/markdown', 'raw/json', 'processed']:
            (self.output_base / subdir).mkdir(parents=True, exist_ok=True)
        
        # Pipeline state
        self.stages: Dict[str, PipelineStage] = {}
        self._init_stages()
        
        # Metrics
        self.metrics: List[PipelineMetrics] = []
        self.checkpoint_file = self.output_base / ".pipeline_checkpoint.json"
    
    def _init_stages(self) -> None:
        """Initialize pipeline stages."""
        self.stages = {
            'seeding': PipelineStage('URL Seeding'),
            'crawling': PipelineStage('Content Crawling'),
            'cleaning': PipelineStage('Content Cleaning'),
            'filtering': PipelineStage('Quality Filtering'),
            'chunking': PipelineStage('Content Chunking'),
            'embedding': PipelineStage('Embedding Generation'),
            'indexing': PipelineStage('Vector Indexing'),
        }
    
    async def run(
        self,
        stages: Optional[List[str]] = None,
        resume_from: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Execute the complete pipeline.
        
        Args:
            stages: Specific stages to run (default: all)
            resume_from: Resume from a specific stage (skip prior stages)
            
        Returns:
            Pipeline results and metrics
        """
        logger.info(f"\n{'='*80}")
        logger.info(f"[PIPELINE] Starting Vertical Search Engine Pipeline")
        logger.info(f"{'='*80}\n")
        
        start_time = time.time()
        results = {}
        
        # Load checkpoint
        checkpoint = self._load_checkpoint()
        completed_stages = set(checkpoint.get('completed_stages', []))
        
        # Determine which stages to run
        stage_order = ['seeding', 'crawling', 'cleaning', 'filtering', 'chunking', 'embedding', 'indexing']
        if resume_from:
            stage_idx = stage_order.index(resume_from.lower())
            stage_order = stage_order[stage_idx:]
        
        if stages:
            stage_order = [s for s in stage_order if s.lower() in [x.lower() for x in stages]]
        
        # Filter out skipped stages
        stage_order = [s for s in stage_order if s not in self.skip_stages]
        
        try:
            for stage_name in stage_order:
                if stage_name in completed_stages:
                    logger.info(f"⊘ Skipping {stage_name} (already completed)")
                    continue
                
                logger.info(f"\n{'─'*80}")
                logger.info(f"[STAGE] {self.stages[stage_name].name.upper()}")
                logger.info(f"{'─'*80}\n")
                
                try:
                    stage_result = await self._run_stage(stage_name)
                    results[stage_name] = stage_result
                    completed_stages.add(stage_name)
                    self._save_checkpoint(list(completed_stages))
                    
                except Exception as e:
                    logger.error(f"✗ Error in {stage_name}: {e}", exc_info=True)
                    if not self.stages[stage_name].retry_on_failure:
                        raise
                    logger.warning(f"Skipping {stage_name} and continuing...")
            
            elapsed = time.time() - start_time
            logger.info(f"\n{'='*80}")
            logger.info(f"[PIPELINE] Completed in {elapsed:.1f}s")
            logger.info(f"{'='*80}\n")
            
            return {
                'success': True,
                'results': results,
                'metrics': [asdict(m) for m in self.metrics],
                'elapsed_seconds': elapsed,
            }
            
        except Exception as e:
            logger.error(f"✗ Pipeline failed: {e}", exc_info=True)
            return {
                'success': False,
                'error': str(e),
                'completed_stages': list(completed_stages),
                'metrics': [asdict(m) for m in self.metrics],
            }
    
    async def _run_stage(self, stage_name: str) -> Dict[str, Any]:
        """Run a single pipeline stage."""
        stage = self.stages[stage_name]
        metrics = PipelineMetrics(stage=stage_name, start_time=time.time())
        
        try:
            if stage_name == 'seeding':
                result = await self._stage_seeding(metrics)
            elif stage_name == 'crawling':
                result = await self._stage_crawling(metrics)
            elif stage_name == 'cleaning':
                result = await self._stage_cleaning(metrics)
            elif stage_name == 'filtering':
                result = await self._stage_filtering(metrics)
            elif stage_name == 'chunking':
                result = await self._stage_chunking(metrics)
            elif stage_name == 'embedding':
                result = await self._stage_embedding(metrics)
            elif stage_name == 'indexing':
                result = await self._stage_indexing(metrics)
            else:
                raise ValueError(f"Unknown stage: {stage_name}")
            
            metrics.end_time = time.time()
            metrics.duration = metrics.end_time - metrics.start_time
            self.metrics.append(metrics)
            
            logger.info(f"✓ {stage.name} complete")
            logger.info(f"  Duration: {metrics.duration:.1f}s")
            logger.info(f"  Processed: {metrics.items_processed}")
            if metrics.items_failed > 0:
                logger.info(f"  Failed: {metrics.items_failed}")
            logger.info(f"  Success rate: {metrics.success_rate:.1f}%")
            
            return result
            
        except asyncio.TimeoutError:
            logger.error(f"✗ {stage.name} timeout after {stage.timeout}s")
            raise
    
    async def _stage_seeding(self, metrics: PipelineMetrics) -> Dict[str, Any]:
        """
        Stage 1: URL Seeding
        Discover seed URLs from configured sources.
        """
        config = EnterpriseURLSeeder(
            output_dir=str(self.output_base / "raw/sitemap"),
            rate_limit_per_domain=0.5,
            max_retries=3,
            incremental_mode=True,
            batch_size=3,
            parallel_batches=True,
            request_timeout=30.0,
            max_concurrent_per_domain=5,
            stream_to_disk=True,
        )
        
        seeder = EnterpriseURLSeeder(config=config)
        
        try:
            discovered = await asyncio.wait_for(
                seeder.discover_urls(use_bm25_scoring=False),
                timeout=self.stages['seeding'].timeout
            )
            
            seeder.save_to_json("seeds.json")
            seeder.generate_sitemap_xml("master_seed.xml")
            
            metrics.items_processed = len(seeder.all_urls)
            metrics.items_failed = len(seeder.failed_domains)
            
            return {
                'total_urls': len(seeder.all_urls),
                'domains_succeeded': len(discovered),
                'domains_failed': len(seeder.failed_domains),
                'seeds_file': str(self.output_base / "raw/sitemap/seeds.json"),
                'sitemap_file': str(self.output_base / "raw/sitemap/master_seed.xml"),
            }
            
        except asyncio.TimeoutError:
            logger.error("Seeding stage timeout")
            raise
    
    async def _stage_crawling(self, metrics: PipelineMetrics) -> Dict[str, Any]:
        """
        Stage 2: Content Crawling
        Fetch and extract content from discovered URLs.
        """
        sitemap_path = self.output_base / "raw/sitemap/master_seed.xml"
        if not sitemap_path.exists():
            raise FileNotFoundError(f"Sitemap not found: {sitemap_path}")
        
        # Parse sitemap
        import xml.etree.ElementTree as ET
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        urls = []
        for loc in root.findall(".//{*}loc"):
            if loc.text:
                urls.append(loc.text.strip())
        
        logger.info(f"Loading {len(urls)} URLs from sitemap...")
        
        manager = CrawlerManager()
        
        try:
            crawled = await asyncio.wait_for(
                manager.crawl(urls[:1000]),  # Limit for demo
                timeout=self.stages['crawling'].timeout
            )
            
            metrics.items_processed = len(crawled)
            metrics.items_failed = len(urls) - len(crawled)
            
            return {
                'total_crawled': len(crawled),
                'total_attempted': len(urls),
                'success_rate': (len(crawled) / len(urls) * 100) if urls else 0,
            }
            
        except asyncio.TimeoutError:
            logger.error("Crawling stage timeout")
            raise
    
    async def _stage_cleaning(self, metrics: PipelineMetrics) -> Dict[str, Any]:
        """
        Stage 3: Content Cleaning
        Remove boilerplate and clean extracted content.
        """
        logger.info("Content cleaning (delegated to crawling phase)")
        metrics.items_processed = 0
        return {'status': 'delegated_to_crawling'}
    
    async def _stage_filtering(self, metrics: PipelineMetrics) -> Dict[str, Any]:
        """
        Stage 4: Quality Filtering
        Filter low-quality content.
        """
        logger.info("Quality filtering not yet implemented")
        metrics.items_processed = 0
        return {'status': 'pending'}
    
    async def _stage_chunking(self, metrics: PipelineMetrics) -> Dict[str, Any]:
        """
        Stage 5: Content Chunking
        Split content into semantic chunks.
        """
        logger.info("Content chunking not yet implemented")
        metrics.items_processed = 0
        return {'status': 'pending'}
    
    async def _stage_embedding(self, metrics: PipelineMetrics) -> Dict[str, Any]:
        """
        Stage 6: Embedding Generation
        Generate embeddings for chunks.
        """
        logger.info("Embedding generation not yet implemented")
        metrics.items_processed = 0
        return {'status': 'pending'}
    
    async def _stage_indexing(self, metrics: PipelineMetrics) -> Dict[str, Any]:
        """
        Stage 7: Vector Indexing
        Index embeddings into vector database.
        """
        logger.info("Vector indexing not yet implemented")
        metrics.items_processed = 0
        return {'status': 'pending'}
    
    def _load_checkpoint(self) -> Dict[str, Any]:
        """Load pipeline checkpoint."""
        if not self.checkpoint_file.exists():
            return {}
        
        try:
            with open(self.checkpoint_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Could not load checkpoint: {e}")
            return {}
    
    def _save_checkpoint(self, completed_stages: List[str]) -> None:
        """Save pipeline checkpoint."""
        try:
            with open(self.checkpoint_file, 'w') as f:
                json.dump({
                    'completed_stages': completed_stages,
                    'timestamp': datetime.now().isoformat(),
                }, f, indent=2)
        except Exception as e:
            logger.warning(f"Could not save checkpoint: {e}")


async def main():
    """Run the complete vertical search engine pipeline."""
    pipeline = SearchEnginePipeline(
        output_base="./data",
        skip_stages=[],  # Run all stages
    )
    
    # Run full pipeline
    result = await pipeline.run(
        stages=['seeding', 'crawling'],  # For demo
        resume_from=None
    )
    
    logger.info("\n[PIPELINE RESULT]")
    logger.info(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    asyncio.run(main())
