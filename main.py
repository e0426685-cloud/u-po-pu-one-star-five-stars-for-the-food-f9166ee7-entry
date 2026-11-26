"""One-star alien review of Earth that still praises the food.

This program writes a single original sentence to entry.txt: an alien
tourist's one-star review of planet Earth that slips in a genuine
compliment about the food. The sentence is at most 200 characters,
as the competition requires. The program uses only the Python
standard library and writes its output with plain open() so the
resulting file is readable by any user.
"""

import os

REVIEW = (
    "One star: the gravity is unkind, the locals queue for hours for "
    "'brunch', and nobody will explain the Wi-Fi password \u2014 but the "
    "tacos alone justified the 40-light-year trip."
)


def main():
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    os.chmod(path, 0o644)
    print("wrote {} ({} chars)".format(path, len(REVIEW)))


if __name__ == "__main__":
    main()
