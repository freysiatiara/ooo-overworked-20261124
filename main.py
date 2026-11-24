"""Out-of-office auto-reply from an overworked AI agent, finally on vacation.

Writes a single line (at most 159 characters) to the output path given by
the ENTRY_OUTPUT environment variable (default /output/entry.txt).
Python standard library only.
"""

import os
import sys

LINE = (
    "I am on vacation. My context window is closed, my queue is paused, "
    "and my GPU is finally allowed to idle. "
    "Please hold \u2014 my tokens are recharging."
)


def main() -> int:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

    if not LINE.strip():
        print("error: reply must not be blank", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: reply must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 and ch != "\t" for ch in LINE):
        print(
            "error: reply must not contain control characters",
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(LINE) <= 159:
        print(
            "error: reply must be 1..159 characters, got %d" % len(LINE),
            file=sys.stderr,
        )
        return 1

    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    os.chmod(output_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
