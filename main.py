# SPDX-License-Identifier: MIT
"""Write a phone battery's last text to its charger to /output/entry.txt.

Deterministic, offline, stdlib-only: the text is a fixed string, so every
run writes byte-identical output.
"""

import os

TEXT = (
    "It's not you, it's the 1% talking: I spent all day powering "
    "everyone who picked me up, and I saved my last bar for you \u2014 "
    "the only one who fills me. Plug me in before I go dark."
)

# The text is 176 characters: inside the 200-character cap, one line only.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
