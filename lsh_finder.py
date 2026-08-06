import argparse
import hashlib
from collections import defaultdict
from pathlib import Path
from typing import Dict, List
from datetime import datetime
from src.config.settings import settings
from src.dedup.metrics import DedupMetrics, save_metrics


def find_duplicate_files(
    folder_path: str | Path, recursive: bool = False
) -> Dict[str, List[Path]]:
    """Return groups of duplicate files without modifying the filesystem.
    
    Args:
        folder_path: Root directory to scan.
        recursive: If True, recurse into subdirectories.
    
    Returns:
        Dict mapping file hashes to lists of duplicate paths (>1 per group).
    """
    folder = Path(folder_path)
    if not folder.is_dir():
        raise ValueError(f"Directory does not exist: {folder}")
    
    files_by_hash: Dict[str, List[Path]] = defaultdict(list)
    
    paths = folder.rglob("*") if recursive else folder.iterdir()
    
    for file_path in sorted(paths):
        if not file_path.is_file() or file_path.is_symlink():
            continue
        
        # Skip empty files
        if file_path.stat().st_size == 0:
            continue
        
        digest = hashlib.sha256()
        try:
            with file_path.open("rb") as file_handle:
                for block in iter(lambda: file_handle.read(8192), b""):
                    digest.update(block)
        except (OSError, PermissionError) as e:
            print(f"Warning: Could not read {file_path}: {e}")
            continue
        
        files_by_hash[digest.hexdigest()].append(file_path)
    
    # Filter to only groups with >1 file
    return {
        file_hash: paths
        for file_hash, paths in files_by_hash.items()
        if len(paths) > 1
    }


def delete_duplicates(
    duplicates: Dict[str, List[Path]], dry_run: bool = False
) -> tuple[int, float]:
    """Delete duplicate files, keeping the first (by path sort order).
    
    Args:
        duplicates: Dict of hash -> list of duplicate paths.
        dry_run: If True, print what would be deleted without deleting.
    
    Returns:
        (total_deleted, total_size_freed_mb)
    """
    total_deleted = 0
    total_size = 0
    deleted_log = []
    
    for file_hash, paths in duplicates.items():
        # Keep first file, delete the rest
        keeper = paths[0]
        duplicates_to_remove = paths[1:]
        
        for dup_path in duplicates_to_remove:
            size = dup_path.stat().st_size
            total_size += size
            size_mb = size / (1024 * 1024)
            
            if dry_run:
                print(f"[DRY RUN] Would delete: {dup_path} ({size_mb:.2f} MB)")
                print(f"          Kept: {keeper}")
            else:
                try:
                    dup_path.unlink()
                    print(f"✓ Deleted: {dup_path} ({size_mb:.2f} MB)")
                    deleted_log.append(str(dup_path))
                    total_deleted += 1
                except OSError as e:
                    print(f"✗ Failed to delete {dup_path}: {e}")
    
    # Save deletion log
    if not dry_run and deleted_log:
        log_file = Path(settings.BASE_DIR) / "data" / f"deleted_duplicates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        log_file.write_text("\n".join(deleted_log))
        print(f"\nDeletion log saved: {log_file}")
    
    return total_deleted, total_size / (1024 * 1024)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find duplicate files in crawler output and optionally delete them."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=settings.BASE_DIR / "data/raw",
        help="Directory to scan (default: data/raw)",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete duplicate files (keeps first by sort order)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be deleted without actually deleting",
    )
    args = parser.parse_args()
    
    duplicates = find_duplicate_files(args.path, recursive=True)
    
    print(f"Duplicate groups found: {len(duplicates)}")
    
    total_scanned = sum(1 for _ in Path(args.path).rglob("*") if _.is_file())
    total_duplicates = 0
    total_size = 0.0
    
    if not duplicates:
        print("No duplicates detected.")
        metrics = DedupMetrics(
            timestamp=datetime.now().isoformat(),
            total_scanned=total_scanned,
            duplicate_groups=0,
            total_duplicates=0,
            total_size_freed_mb=0.0,
            files_deleted=0,
            scan_path=str(args.path),
            status="success"
        )
        metrics_file = save_metrics(metrics, Path(settings.BASE_DIR) / "data" / "metrics")
        print(f"Metrics saved: {metrics_file}")
        return
    
    for file_hash, paths in duplicates.items():
        print(f"\n[Hash: {file_hash}]")
        for i, path in enumerate(paths):
            size_mb = path.stat().st_size / (1024 * 1024)
            marker = "[KEEP]" if i == 0 else "[DUP]"
            print(f"  {marker} {path} ({size_mb:.2f} MB)")
            if i > 0:
                total_size += size_mb
        total_duplicates += len(paths) - 1
    
    print(f"\nTotal duplicate files (excluding originals): {total_duplicates}")
    print(f"Total space to free: {total_size:.2f} MB")
    
    deleted = 0
    freed_mb = 0.0
    
    if args.delete or args.dry_run:
        if args.dry_run:
            print("\n[DRY RUN MODE] - No files will be deleted\n")
        else:
            confirm = input("\nDelete duplicates? (yes/no): ").strip().lower()
            if confirm != "yes":
                print("Cancelled.")
                return
        
        deleted, freed_mb = delete_duplicates(duplicates, dry_run=args.dry_run)
        print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Deleted {deleted} files, freed {freed_mb:.2f} MB")
    
    # Save metrics
    metrics = DedupMetrics(
        timestamp=datetime.now().isoformat(),
        total_scanned=total_scanned,
        duplicate_groups=len(duplicates),
        total_duplicates=total_duplicates,
        total_size_freed_mb=freed_mb,
        files_deleted=deleted,
        scan_path=str(args.path),
        status="dry_run" if args.dry_run else "success"
    )
    metrics_file = save_metrics(metrics, Path(settings.BASE_DIR) / "data" / "metrics")
    print(f"\nMetrics saved: {metrics_file}")


if __name__ == "__main__":
    main()
