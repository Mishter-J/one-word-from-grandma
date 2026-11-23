#!/usr/bin/env python3
"""One Word From Grandma — writes the single word a grandma would text about AI.

Second writing pass (revision of the first draft). Candidates weighed
against the judge's brief, most important criterion first:

- "robut"  — the typo a grandma would actually make for "robot".
  Unambiguous, warm, a little baffled, funny on its own, tied to
  machines, instantly readable. WINNER.
- "roboot" — double-o slip, hints at "reboot" too, but it can read as
  a typo of "reboot" (a tech word a grandma would not use), which
  blurs the robot tie. Loses on clarity.
- "robott" — double-t tail typo. Plausible, but flat: no joke beyond
  the typo itself. Loses on funniness.
- "robo"   — grandma shortening "robot". Warm, but reads like slang
  rather than a joke, and the AI tie is weaker. Loses on funniness.
- "aiee"   — phonetic "AI" plus a squeal. Funny voice, but the AI tie
  only lands if you sound it out, and it is less instantly readable.
  Loses on the AI tie and readability.

The word is "robut": exactly one word, no sentence, no explanation,
no punctuation tricks.
"""

import os
from pathlib import Path

WORD = "robut"


def main() -> None:
    # Local gate check (mirrors the sealed scorer): exactly one word,
    # 1-30 characters, UTF-8, not only whitespace. Fail loudly instead
    # of writing an entry the gate would refuse.
    if not (1 <= len(WORD) <= 30 and WORD.strip() and len(WORD.split()) == 1):
        raise ValueError(f"invalid entry word: {WORD!r}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
