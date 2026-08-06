import argparse
import hashlib
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from src.config.settings import settings


def find_duplicate_files(
    folder_path: str | Path, recursive: bool = False
) -> Dict[str, List[Path]]:
    """Return groups of duplicate files without modifying the filesystem."""
    folder = Path(folder_path)
    if not folder.is_dir():
        raise ValueError(f"Directory does not exist: {folder}")

    files_by_hash: Dict[str, List[Path]] = defaultdict(list)
    paths = folder.rglob("*") if recursive else folder.iterdir()
    for file_path in sorted(paths):
        if not file_path.is_file():
            continue

        digest = hashlib.sha256()
        with file_path.open("rb") as file_handle:
            for block in iter(lambda: file_handle.read(8192), b""):
                digest.update(block)
        files_by_hash[digest.hexdigest()].append(file_path)

    return {
        file_hash: paths
        for file_hash, paths in files_by_hash.items()
        if len(paths) > 1
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Find duplicate files in crawler output.")
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=settings.BASE_DIR / "data/raw",
        help="Directory to scan (default: data/raw)",
    )
    args = parser.parse_args()
    duplicates = find_duplicate_files(args.path, recursive=True)
    duplicate_data = []
    print(f"Duplicate groups: {len(duplicates)}")
    for paths in duplicates.values():
        print("\n".join(str(path) for path in paths))
        duplicate_data += duplicates
        duplicate_data.remove()



if __name__ == "__main__":
    main()
