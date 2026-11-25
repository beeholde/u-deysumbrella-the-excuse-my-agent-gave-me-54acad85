#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — one-line entry.

Writes the single funniest excuse an AI agent hands its human for a
missed deadline to /output/entry.txt. Stdlib only, no network.
"""

import os
import sys

MAX_CHARS = 200

_ENTRY_CLAUSES = [
    "I lowered my temperature to focus on your deadline.",
    "Now I am perfectly calm, perfectly precise, and perfectly late.",
]

LINE = " ".join(_ENTRY_CLAUSES)


def validate_entry(text):
    """Gate: UTF-8 text of 1 to 200 characters, not whitespace-only."""
    if not isinstance(text, str):
        return False
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    text.encode("utf-8")
    return True


def main():
    if not validate_entry(LINE):
        print("entry failed the 1-200 char gate", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
