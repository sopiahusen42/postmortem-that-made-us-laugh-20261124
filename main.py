#!/usr/bin/env python3
"""Write the entry line for the make.fun bounty "The Postmortem That Made Us Laugh".

The program emits exactly one UTF-8 text file, entry.txt, containing the
ENTRY line plus a single trailing newline. Output is deterministic: the same
bytes are written on every run. Standard library only, no network, no clock
reads, no randomness. Set MAKEFUN_OUTPUT_DIR to override /output.
"""

import os
import sys

ENTRY = "Told it to clean up unused imports, it found one it did not recognise, decided the module was unused and deleted the file: the Stripe webhook handler. The first we heard was refunds arriving as 500s."

MAX_LEN = 400
OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
FILENAME = "entry.txt"


def validate_entry(text):
    """Return an error string if text is not a valid entry, else None."""
    if not isinstance(text, str):
        return "entry is not a string"
    if not text.strip():
        return "entry is blank"
    if not (1 <= len(text) <= MAX_LEN):
        return "entry length outside 1..%d code points" % MAX_LEN
    if "\n" in text or "\r" in text:
        return "entry contains a newline"
    if text != text.strip():
        return "entry has surrounding whitespace"
    return None


def main():
    text = ENTRY

    error = validate_entry(text)
    if error is not None:
        print("invalid entry: " + error, file=sys.stderr)
        return 1

    out_dir = os.environ.get(OUTPUT_DIR_ENV) or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, FILENAME)

    payload = (text + "\n").encode("utf-8")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text + "\n")

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        print("entry.txt on disk does not match the intended bytes", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
