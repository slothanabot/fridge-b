"""Notes From a Passive-Aggressive Fridge.

Writes one single line — a note left by a smart fridge for its owner —
to entry.txt in the output directory given by MAKEFUN_OUTPUT_DIR
(default "/output").

The note: the owner left the door open again, the ice cream melted into
soup, there is a puddle on the floor, and the fridge's door alarm logged
every second of it. The fridge keeps receipts.
"""

import os

ENTRY = (
    "Door open 47 minutes. The ice cream is soup, the floor is a puddle, "
    "and my door alarm has logged every second of it. I keep receipts."
)

MAX_CHARS = 200


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) > MAX_CHARS:
        raise SystemExit(f"entry is {len(body)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    """Validate the line, then write it to entry.txt."""
    body = ENTRY
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) > MAX_CHARS:
        raise SystemExit(f"entry is {len(body)} chars, over the {MAX_CHARS} limit")
    body.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(body + "\n")
    verify(path, body)


if __name__ == "__main__":
    main()
