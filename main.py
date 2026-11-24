#!/usr/bin/env python3
"""Duskline Warning Label — make.fun entry.

Writes one single-line safety warning label for human beings to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./out/entry.txt when the variable is
unset, for local testing only). Standard library only, deterministic,
no network access. The entry text is a fixed constant: the program
never reads anything from outside itself.
"""

import os
import sys

ENTRY_TEXT = (
    "WARNING: human contains unpatched optimism, runs on caffeine, "
    "and will say five more minutes for up to three hours."
)

MAX_CHARS = 160


def _validate_entry(text: str) -> None:
    """Assert the entry text satisfies the competition gate.

    The gate requires UTF-8 text of 1 to 160 characters, not only
    white space, on a single line. Raises AssertionError otherwise.
    """
    assert isinstance(text, str), "entry text must be a string"
    assert text, "entry text must not be empty"
    assert text.strip(), "entry text must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
    )
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    _validate_entry(ENTRY_TEXT)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY_TEXT, "written entry differs from ENTRY_TEXT"
    return 0


if __name__ == "__main__":
    sys.exit(main())
