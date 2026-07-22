import hashlib
from collections import defaultdict
from pathlib import Path
from typing import Dict, List


def find_duplicate_files(folder_path: str | Path) -> Dict[str, List[Path]]:
    """Return groups of duplicate files without modifying the filesystem."""
    folder = Path(folder_path)
    if not folder.is_dir():
        raise ValueError(f"Directory does not exist: {folder}")

    files_by_hash: Dict[str, List[Path]] = defaultdict(list)
    for file_path in sorted(folder.iterdir()):
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
