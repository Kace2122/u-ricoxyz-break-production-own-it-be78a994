#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line.

An AI agent prints this the instant it breaks production.
"""
import os

ENTRY = "I rotated the production API key in the deploy and forgot to tell production. It has been locked out of itself for four hours."

def main():
    # Gate: the confession must be one line, 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
