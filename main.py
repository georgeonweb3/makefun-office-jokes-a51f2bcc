#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single original funny line of text to /output/entry.txt:
an expense claim for a stapler, approved as "morale infrastructure"
in four minutes, against a raise request gathering dust under
Dave's lunch. The raise is the punchline, never the setup.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "I expensed a stapler as morale infrastructure and Finance approved "
    "it in four minutes; my raise request is still sitting on Dave's "
    "desk, under his lunch."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 199 characters, not only whitespace — and one line:
    # an embedded newline would split the joke and break the gate.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate wants 1-199"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
