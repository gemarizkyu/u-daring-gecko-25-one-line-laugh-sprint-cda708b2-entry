#!/usr/bin/env python3
"""Write the one-line joke to /output/entry.txt.

Deterministic: the same single line every run.
No network, no randomness, no wall clock, no model calls.
"""

import os

LINE = "My fitness tracker congratulated me for standing up, which is the first time anyone has ever applauded me for doing the absolute bare minimum."
# The line is one sentence, 142 characters, inside the 1-200 character gate.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
