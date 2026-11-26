#!/usr/bin/env python3
"""One Line, One Laugh — write a single funny line to /output/entry.txt.

The joke is a fixed, deterministic string: no randomness, no network,
no clock, no input. Every run writes exactly the same bytes.
"""

import os

JOKE = (
    "I went to therapy to stop talking to myself, "
    "and now I pay someone to listen to me do it professionally."
)


def main() -> None:
    # Guard the competition gate in code: 1 to 140 characters, one line.
    assert 1 <= len(JOKE) <= 140, "joke must be 1-140 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write plain UTF-8 text, one line, no trailing newline: the gate
    # counts characters, and a trailing newline would count too.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
