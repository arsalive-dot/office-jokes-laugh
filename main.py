"""Make the AI Judge Laugh: Office Jokes — one-line office joke entry.

The entry is a single line about office life, under 200 characters.
It writes the joke to /output/entry.txt deterministically.

Craft: the joke turns on HR treating a dead office plant like an
underperforming employee — recognition (the PIP) with the surprise
saved for the last words, and no Monday-morning or photocopier cliché.
"""

import os


ENTRY = "Our office plant died, so HR put it on a performance improvement plan."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
