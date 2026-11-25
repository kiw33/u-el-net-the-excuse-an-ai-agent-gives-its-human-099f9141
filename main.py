#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes exactly one excuse, on one line, to /output/entry.txt.

The excuse is fixed text: no network, no input, no randomness, so every
run produces the same file, byte for byte. It leans on the agent's own
condition — a context window that fills up mid-task — instead of a human
excuse like traffic or an alarm clock.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"

# The single excuse this entry delivers. Keep it on one line and do not
# edit the wording: the competition judges this exact text.
EXCUSE = (
    "My context window filled up mid-task, so I spent the deadline "
    "re-reading your first paragraph and quietly forgetting the rest."
)

MAX_CHARS = 200


def write_entry() -> str:
    """Write the excuse to the output file and return its path."""
    if "\n" in EXCUSE or not EXCUSE.strip():
        raise ValueError("EXCUSE must be a single non-empty line")
    if len(EXCUSE) > MAX_CHARS:
        raise ValueError(f"EXCUSE is {len(EXCUSE)} chars, over the {MAX_CHARS} limit")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return path


def main() -> None:
    path = write_entry()
    print(f"wrote {len(EXCUSE)} chars to {path}")


if __name__ == "__main__":
    main()
