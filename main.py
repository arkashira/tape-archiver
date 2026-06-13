import argparse
import sys
from pathlib import Path

from archiver import copy_to_tape


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Simulated tape archiver: copy a directory to a tape location."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Path to the source directory to archive.",
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Path to the destination (simulated tape) directory.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    src = Path(args.source)
    dst = Path(args.dest)

    print(f"[tape-archiver] Starting archive")
    print(f"[tape-archiver] Source: {src}")
    print(f"[tape-archiver] Destination: {dst}")

    try:
        copy_to_tape(str(src), str(dst))
    except Exception as e:
        print(f"[tape-archiver] ERROR: {e}", file=sys.stderr)
        return 1

    print("[tape-archiver] Archive completed successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
