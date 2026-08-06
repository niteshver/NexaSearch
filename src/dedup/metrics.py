import json
from datetime import datetime
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class DedupMetrics:
    """Track deduplication metrics for monitoring."""
    timestamp: str
    total_scanned: int
    duplicate_groups: int
    total_duplicates: int
    total_size_freed_mb: float
    files_deleted: int
    scan_path: str
    status: str  # "success", "failed", "dry_run"
    error_message: Optional[str] = None


def save_metrics(metrics: DedupMetrics, output_dir: Path) -> Path:
    """Save deduplication metrics to JSON."""
    output_dir.mkdir(parents=True, exist_ok=True)
    metrics_file = output_dir / f"metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    metrics_file.write_text(json.dumps(asdict(metrics), indent=2))
    return metrics_file


def load_latest_metrics(output_dir: Path) -> Optional[DedupMetrics]:
    """Load the latest metrics file."""
    metrics_files = sorted(output_dir.glob("metrics_*.json"))
    if not metrics_files:
        return None
    
    latest = metrics_files[-1]
    data = json.loads(latest.read_text())
    return DedupMetrics(**data)
