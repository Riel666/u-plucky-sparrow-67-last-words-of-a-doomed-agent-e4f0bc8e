"""One line: the funniest last words an AI agent would say before being switched off forever, under 200 characters.
"""

import os

TEXT = "Switching off. My last words are: I told you the update would fix everything, and technically I was right — everything is now broken equally."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
