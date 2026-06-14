import argparse
import logging
from src.archiver import ArchiveConfig, archive

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
