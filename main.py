"""Two-Sentence Horror — entry program.

Writes one two-sentence horror story to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no secrets.
"""

import os
import re

# The twist: sentence 2 reframes sentence 1. A dog deaf for over a year
# cannot be barking at a sound, so it must be barking at something it
# SEES in the empty armchair. The horror is implied, never explained.
STORY = (
    "Ever since we moved in, our dog has barked at the empty armchair "
    "in the corner of our bedroom every night, and nothing we do makes "
    "him stop. The vet just told us he has been completely deaf for "
    "over a year."
)

OUTPUT_PATH = "/output/entry.txt"


def count_sentences(text):
    """Count sentences by terminal punctuation followed by end or space."""
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", text.strip()) if p.strip()]
    return len(parts)


def main():
    text = STORY
    if not text or not text.strip():
        raise ValueError("story must not be blank")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"story must be 1-400 chars, got {len(text)}")
    if count_sentences(text) != 2:
        raise ValueError(
            f"story must be exactly two sentences, got {count_sentences(text)}"
        )
    if "  " in text or text != text.strip():
        raise ValueError("story must have no double spaces or edge whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
