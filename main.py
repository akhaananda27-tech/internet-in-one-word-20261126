#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The Internet in One Word — prints the single word that describes the whole internet."""

from pathlib import Path

WORD_FILE = Path(__file__).parent / "word.txt"


def main() -> None:
    word = WORD_FILE.read_text(encoding="utf-8").strip()
    print(word)


if __name__ == "__main__":
    main()
