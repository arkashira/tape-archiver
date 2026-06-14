import os
import pytest
from src.archiver import ArchiveConfig, archive
from tempfile import TemporaryDirectory

def test_archive(tmp_path):
    source_dir = tmp_path / "source"
    destination_dir = tmp_path / "destination"
    source_dir.mkdir()
    destination_dir.mkdir()
    file_path = source_dir / "file.txt"
    file_path.write_text("Hello, World!")
    config = ArchiveConfig(str(source_dir), str(destination_dir))
    archive(config)
    assert (destination_dir / "file.txt").exists()
    assert (destination_dir / "file.txt").read_text() == "Hello, World!"

def test_archive_subdir(tmp_path):
    source_dir = tmp_path / "source"
    destination_dir = tmp_path / "destination"
    source_dir.mkdir()
    destination_dir.mkdir()
    subdir = source_dir / "subdir"
    subdir.mkdir()
    file_path = subdir / "file.txt"
    file_path.write_text("Hello, World!")
    config = ArchiveConfig(str(source_dir), str(destination_dir))
    archive(config)
    assert (destination_dir / "subdir" / "file.txt").exists()
    assert (destination_dir / "subdir" / "file.txt").read_text() == "Hello, World!"

def test_archive_empty_source(tmp_path):
    source_dir = tmp_path / "source"
    destination_dir = tmp_path / "destination"
    source_dir.mkdir()
    destination_dir.mkdir()
    config = ArchiveConfig(str(source_dir), str(destination_dir))
    archive(config)
    assert not os.listdir(destination_dir)

def test_archive_invalid_source(tmp_path):
    source_dir = tmp_path / "source"
    destination_dir = tmp_path / "destination"
    destination_dir.mkdir()
    config = ArchiveConfig(str(source_dir), str(destination_dir))
    with pytest.raises(FileNotFoundError):
        archive(config)
