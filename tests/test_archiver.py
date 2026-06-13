import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

from archiver import copy_to_tape


def create_file(path: Path, content: str = "data"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def test_copy_to_tape_preserves_structure():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        src_path = Path(src_dir)
        # create nested files
        create_file(src_path / "a.txt")
        create_file(src_path / "sub/b.txt")
        create_file(src_path / "sub/c/d.txt", "deep")

        copy_to_tape(str(src_path), str(dst_dir))

        dst_path = Path(dst_dir)
        assert (dst_path / "a.txt").exists()
        assert (dst_path / "sub/b.txt").exists()
        assert (dst_path / "sub/c/d.txt").read_text() == "deep"


def test_cli_successful_execution():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        src_path = Path(src_dir)
        create_file(src_path / "file.txt", "hello")

        result = subprocess.run(
            [sys.executable, "main.py", "--source", src_dir, "--dest", dst_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        assert result.returncode == 0
        # basic sanity check on output
        assert "[tape-archiver] Starting archive" in result.stdout
        assert "[tape-archiver] Archive completed successfully" in result.stdout

        # verify file copied
        assert (Path(dst_dir) / "file.txt").read_text() == "hello"
