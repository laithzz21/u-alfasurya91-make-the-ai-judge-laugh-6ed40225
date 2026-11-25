#!/usr/bin/env python3
"""Entry generator for the make.fun bounty
'u-alfasurya91-make-the-ai-judge-laugh-6ed40225'.

The brief: ONE joke about office life, ONE line, UNDER 200 characters.
The judge weighs truth to office life, a surprising turn, a tight
line, and freshness.

The entry opens on the most overused line in office life — "we're a
family here" — and then takes it literally: if it really is a family,
you can't choose your coworkers, you can't leave, and Dad (the boss)
decides your allowance (your salary). The punch lands on "Dad decides
my allowance", a literal-family twist on the corporate family cliché.

Deterministic, stdlib only, no network, no clock, no randomness.
`main.py` validates the entry against every rule in the brief, prints
it to stdout, and writes it to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT` when set, otherwise a per-entry `output` directory
next to this script).
"""

import os
import sys

SLUG = "u-alfasurya91-make-the-ai-judge-laugh-6ed40225"
MAX_CHARS = 200

ENTRY_TEXT = (
    "My boss says we're a family here \u2014 which explains why I can't "
    "choose my coworkers, can't leave, and Dad decides my allowance."
)


def validate(text):
    """Check the entry against every rule in the brief."""
    if not text or not text.strip():
        return "entry is empty"
    if len(text) >= MAX_CHARS:
        return "entry is %d chars, must be under %d" % (len(text), MAX_CHARS)
    if "\n" in text.strip():
        return "entry must be a single line"
    if "family" not in text.lower():
        return "entry must play on office life"
    if not has_surprising_turn(text):
        return "entry needs a surprising turn, not just the setup"
    return None


def has_surprising_turn(text):
    """The twist must reframe the setup: the boss becomes Dad and the
    salary becomes an allowance, so the corporate cliché collapses
    into a literal family."""
    lowered = text.lower()
    return "dad" in lowered and "allowance" in lowered


def main():
    error = validate(ENTRY_TEXT)
    if error:
        print("INVALID ENTRY: %s" % error, file=sys.stderr)
        return 1
    print(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT")
    if not out_dir:
        # Fallback: per-entry output directory next to this script, so
        # parallel authors never share one output path.
        out_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
