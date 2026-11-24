#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

Standard library only, no network. The text is written as raw UTF-8 bytes,
with no trailing newline, into the folder named by MAKEFUN_OUTPUT_DIR when
that variable is set and into /output otherwise. The character count goes
to stderr so stdout stays empty.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "My agent scheduled the deploy for end of day, "
    "defined end of day as 11:40, and went to lunch."
)

ENTRY_NAME = "entry.txt"


def resolve_output_dir() -> Path:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, then /output."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    return Path(folder or "/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be between 1 and 280 characters"

    folder = resolve_output_dir()
    folder.mkdir(parents=True, exist_ok=True)

    entry = folder / ENTRY_NAME
    entry.write_bytes(text.encode("utf-8"))

    count = len(text)
    print(count, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
