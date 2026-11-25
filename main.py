#!/usr/bin/env python3
"""Fix Human Sleep — funniest patch note entry.

Writes a single line of patch notes to /output/entry.txt.
"""

import os

ENTRY = "v1.0.1 — Fixed: human sleep no longer freezes at 3 a.m. to replay every embarrassing thing you said in 2009."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
