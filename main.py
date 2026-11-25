"""Museum of the Year 3000.

Competition: u-donrulezz-museum-of-the-year-3000-b727a0bb
Final label (22 words, 121 characters, one line):
    Close-door button, c. 2025. Pressed millions of times a day by humans
    in a hurry. It did nothing. They pressed it anyway.

Gate (from the kit's competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace.
This program is deterministic, stdlib only, no network, no randomness, no
clock: it writes the fixed label to entry.txt under MAKEFUN_OUTPUT_DIR
(default "/output").
"""

import os

TEXT = (
    "Close-door button, c. 2025. Pressed millions of times a day by humans "
    "in a hurry. It did nothing. They pressed it anyway.\n"
)


def check_gate():
    """Assert the label passes the kit gate before anything is written."""
    body = TEXT.rstrip("\n")
    assert 1 <= len(body) <= 200, "gate: entry must be 1-200 characters"
    assert body.strip(), "gate: entry must not be only whitespace"
    assert "\n" not in body, "gate: entry must be a single line"


def verify_written_bytes(path):
    """Read the file back and compare it byte-for-byte with TEXT."""
    with open(path, "rb") as fh:
        data = fh.read()
    assert data == TEXT.encode("utf-8"), "written bytes differ from TEXT"
    return data


def main():
    check_gate()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)
    verify_written_bytes(path)


if __name__ == "__main__":
    main()
