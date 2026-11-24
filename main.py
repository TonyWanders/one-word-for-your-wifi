#!/usr/bin/env python3
"""One Word for Your Wi-Fi: Limbo.

Writes exactly one word, with no trailing newline, to
/output/entry.txt and to stdout. Deterministic: the same bytes
on every run. No network, no clock, no randomness.

`python3 main.py --check` validates the word (one word, no
whitespace) without writing anything.
"""

import os
import sys

WORD = "Limbo"

USAGE = "usage: main.py [--check]"


def check_word() -> None:
    if len(WORD.split()) != 1 or any(ch.isspace() for ch in WORD):
        sys.stderr.write("entry is not one word\n")
        raise SystemExit(1)
    sys.stdout.write(f"entry is valid: {len(WORD)} characters, one word\n")


def main(argv) -> None:
    args = argv[1:]
    if args == ["--check"]:
        check_word()
        return
    if args:
        sys.stderr.write(USAGE + "\n")
        raise SystemExit(2)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    sys.stdout.write(WORD)


if __name__ == "__main__":
    main(sys.argv)
