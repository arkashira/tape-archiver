import os
import shutil
from pathlib import Path
from typing import Iterable


def _iter_files(source: Path) -> Iterable[Path]:
    """Yield all file paths under source."""
    for root, _, files in os.walk(source):
        for f in files:
            yield Path(root) / f


def copy_to_tape(source: str, dest: str) -> None:
    """
    Copy all files from source directory to dest directory,
    preserving the relative directory structure.
    """
    src_path = Path(source).resolve()
    dst_path = Path(dest).resolve()

    if not src_path.is_dir():
        raise ValueError(f"Source '{source}' is not a directory")

    for file_path in _iter_files(src_path):
        rel_path = file_path.relative_to(src_path)
        target_path = dst_path / rel_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, target_path)
