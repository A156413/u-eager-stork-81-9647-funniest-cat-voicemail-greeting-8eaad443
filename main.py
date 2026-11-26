#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting entry (program/v1).

Writes one original voicemail greeting, as spoken by a cat, to
/output/entry.txt. The greeting must be UTF-8 text of 1 to 120
characters, a single line, with no trailing newline.
"""

import os

ENTRY_TEXT = "Hi, you've reached the cat. I'm asleep on your keyboard — leave a message and I'll ignore it with great enthusiasm."


def main():
    # The sealed scorer gates on 1-120 characters; refuse to write
    # anything that would fail the gate instead of shipping it.
    if not 1 <= len(ENTRY_TEXT) <= 120 or not ENTRY_TEXT.strip():
        raise SystemExit("entry fails the 1-120 character gate")
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
