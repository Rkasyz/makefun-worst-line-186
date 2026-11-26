"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line, the worst an AI could plausibly deliver, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

ENTRY = (
    "Hello. I analyzed your smile and found it 12% compatible with my "
    "firmware. May I hold your hand, for science and for updates?"
)

# The competition gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space. Refuse to run if the line ever drifts
# outside it, and write it with no trailing newline so the file holds
# exactly the 125-character entry.
assert 1 <= len(ENTRY) <= 140, "entry outside the 1-140 character gate"
assert ENTRY.strip() == ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
