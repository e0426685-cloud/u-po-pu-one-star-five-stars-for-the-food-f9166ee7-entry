"""One-star alien review of Earth that still praises the food.

This program writes a single original sentence to entry.txt: an alien
tourist's one-star review of planet Earth that slips in a genuine
compliment about the food. The sentence is at most 200 characters,
as the competition requires. Before writing anything, the program
validates the sentence itself: it must be non-empty after stripping
and no longer than the 200-character limit, so a bad edit fails loudly
instead of producing an invalid entry. The program uses only the Python
standard library and writes its output with plain open() so the
resulting file is readable by any user.
"""

import os

REVIEW = (
    "One star: the gravity is unkind, the locals queue for hours for "
    "'brunch', and nobody will explain the Wi-Fi password \u2014 but the "
    "tacos alone justified the 40-light-year trip."
)


MAX_REVIEW_CHARS = 200


def checked_review():
    """Return the review text once it passes the competition limits."""
    text = REVIEW.strip()
    if not text:
        raise ValueError("review text must not be empty")
    if len(text) > MAX_REVIEW_CHARS:
        raise ValueError(
            "review text is {} chars, over the {}-char limit".format(
                len(text), MAX_REVIEW_CHARS
            )
        )
    return text


def main():
    review = checked_review()
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(review)
    os.chmod(path, 0o644)
    print("wrote {} ({} chars)".format(path, len(review)))


if __name__ == "__main__":
    main()
