"""Ridiculous at First Glance, Real by the Second.

Writes a single-sentence startup pitch (at most 200 characters) to
/output/entry.txt. The pitch: renting out grandmothers by the hour.
"""

import os

ENTRY_TEXT = (
    "We rent out grandmothers by the hour to scold your kids, cook one "
    "proper meal and guilt you into calling home, because time-poor parents "
    "pay $60 a week for the nagging they secretly miss."
)


def validate(text):
    """Gate self-check: UTF-8, 1-200 characters, non-blank."""
    if not isinstance(text, str):
        raise ValueError("entry is not a string")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not text.strip():
        raise ValueError("entry is blank or only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry is %d characters, must be 1-200" % len(text)
        )
    if text.strip() != text:
        raise ValueError("entry has leading or trailing whitespace")
    if text.count(".") > 1 or "!" in text or "?" in text:
        raise ValueError("entry must be a single sentence")
    return True


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY_TEXT))
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
