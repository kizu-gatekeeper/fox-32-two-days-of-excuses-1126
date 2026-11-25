"""Entry for make.fun bounty: Two Days of Excuses.

Writes one single-line AI excuse for a missed deadline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

LINE = "I missed the deadline because I confidently hallucinated the finished report, then spent two days deleting it one plausible paragraph at a time."
MAX_CHARS = 200


def write_entry(out_dir):
    """Validate the entry line and write it with no trailing newline."""
    if not LINE or not LINE.strip():
        raise ValueError("entry must be non-empty")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
