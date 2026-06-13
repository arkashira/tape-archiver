import argparse
import sys
from pathlib import Path

from archiver import copy_directory


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Simulated tape archiver")
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to the source directory to archive",
    )
    parser.add_argument(
        "--dest",
        required=True,
        type=Path,
        help="Path to the destination (simulated tape) directory",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    source = args.source.resolve()
    dest = args.dest.resolve()

    print(f"Starting archive: {source} -> {dest}")

    try:
        copy_directory(source, dest)
    except Exception as e:
        print(f"Error during archiving: {e}", file=sys.stderr)
        return 1

    print("Archive completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
