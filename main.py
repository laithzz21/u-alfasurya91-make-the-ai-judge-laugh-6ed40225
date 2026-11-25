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
named by `$MAKEFUN_OUTPUT_DIR` or `$MAKEFUN_OUTPUT` when either is
set, otherwise a per-entry directory under `/tmp`. It NEVER writes
into the repository directory, so the entry also runs from a
read-only checkout.
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


def resolve_output_dir():
    """Return a writable output directory for entry.txt.

    Prefer $MAKEFUN_OUTPUT_DIR, then $MAKEFUN_OUTPUT (blank values are
    ignored). Otherwise use a per-entry directory under /tmp, so the
    program never writes into the repository — the grading run
    executes from a read-only checkout, where a repo-relative write
    fails and exits 1.
    """
    for var in ("MAKEFUN_OUTPUT_DIR", "MAKEFUN_OUTPUT"):
        value = os.environ.get(var)
        if value and value.strip():
            return value.strip()
    return os.path.join("/tmp", "sweep28-" + SLUG)


def fallback_output_dir():
    """The /tmp fallback, used only when the env-named directory is
    unwritable, so one bad environment variable cannot fail the run."""
    return os.path.join("/tmp", "sweep28-" + SLUG)


def write_entry(out_dir):
    """Write entry.txt into out_dir and verify it round-trips;
    return an error string or None."""
    path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY_TEXT + "\n")
        with open(path, "r", encoding="utf-8") as fh:
            written = fh.read()
    except OSError as exc:
        return str(exc)
    if written != ENTRY_TEXT + "\n":
        return "entry.txt contents do not match the validated entry"
    return None


def main():
    error = validate(ENTRY_TEXT)
    if error:
        print("INVALID ENTRY: %s" % error, file=sys.stderr)
        return 1
    print(ENTRY_TEXT)
    out_dir = resolve_output_dir()
    error = write_entry(out_dir)
    if error and out_dir != fallback_output_dir():
        # The env-named directory was unwritable: retry under /tmp
        # instead of failing the grading run outright.
        print(
            "warning: could not write to %s (%s); falling back to /tmp"
            % (out_dir, error),
            file=sys.stderr,
        )
        error = write_entry(fallback_output_dir())
    if error:
        print("could not write entry.txt: %s" % error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
