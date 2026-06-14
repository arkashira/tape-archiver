import argparse
import logging
import os
import shutil
from dataclasses import dataclass
from typing import List

@dataclass
class ArchiveConfig:
    source: str
    destination: str

def archive(config: ArchiveConfig) -> None:
    """
    Copy all files from `config.source` to `config.destination`, preserving
    directory structure. Raises FileNotFoundError if the source directory
    does not exist.
    """
    logging.info(f"Archiving {config.source} to {config.destination}")

    # Validate source directory exists
    if not os.path.isdir(config.source):
        raise FileNotFoundError(f"Source directory not found: {config.source}")

    for root, dirs, files in os.walk(config.source):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(root, config.source)
            destination_dir = os.path.join(config.destination, relative_path)
            os.makedirs(destination_dir, exist_ok=True)
            destination_file = os.path.join(destination_dir, file)
            shutil.copy2(source_file, destination_file)
            logging.info(f"Copied {source_file} to {destination_file}")
    logging.info("Archiving complete")

def main() -> None:
    parser = argparse.ArgumentParser(description="Tape Archiver")
    parser.add_argument("--source", required=True, help="Source directory")
    parser.add_argument("--dest", required=True, help="Destination directory")
    args = parser.parse_args()
    config = ArchiveConfig(args.source, args.dest)
    archive(config)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
