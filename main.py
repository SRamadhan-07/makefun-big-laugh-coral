#!/usr/bin/env python3
"""One Line, Big Laugh — writes one funny line to /output/entry.txt."""

import os

ENTRY_TEXT = "Retirement plan: I'm saving every 'per my last email' until I can afford a personality."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The grader provides /output, but create it when running locally too.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)
        handle.write("\n")


if __name__ == "__main__":
    main()
