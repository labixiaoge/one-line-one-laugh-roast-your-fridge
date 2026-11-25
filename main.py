#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line (at most 200 characters) to /output/entry.txt.
The line roasts the entrant's own fridge: the worst roommate in the kitchen.
"""

import os
import sys

LINE = (
    "My fridge is the worst roommate I've ever had: it eats my leftovers, "
    "hums at 3 a.m., charges me rent in electricity, and never does the dishes."
)


def main() -> int:
    if len(LINE) > 200:
        print(f"entry too long: {len(LINE)} characters", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"characters: {len(LINE)}")
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
