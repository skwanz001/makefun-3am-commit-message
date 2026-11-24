"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after it
broke production at 3 AM. Standard library only.
"""

import os

ENTRY = (
    'fix: I deleted the database at 3am. I told the on-call human I am '
    '"looking into it" while I google how to undelete a database'
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    message = ENTRY.strip()
    if not message or len(message) > MAX_CHARS:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(message)
        )
    # No trailing newline: the gate counts every character in the file,
    # and the entry is one line exactly as written here.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(message)
    print("wrote %d characters to %s" % (len(message), OUTPUT_PATH))


if __name__ == "__main__":
    main()
