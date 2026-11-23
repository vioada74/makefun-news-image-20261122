"""Copy the entry image to the output directory.

The entry is a pre-rendered PNG (entry.png, next to this file) that sums
up the world news of Sunday 22 November 2026 as a newspaper front
page: masthead, date band, a full-width hero lead with a headline in
larger type, seven more photo stories with at most 12 words each, and
a footer ticker. The hero is COP31 collapsing with no deal in Antalya;
the other stories are the tanker attacks near the Strait of Hormuz, a
Russian drone hitting a block of flats near Kyiv, BepiColombo reaching
Mercury, Marc Marquez sealing his eighth MotoGP title, the Democrats
taking 258 House seats, the FBI crime database breach, and a funeral
boat sinking in Nigeria. This program only copies it to
$MAKEFUN_OUTPUT_DIR/entry.png, so both runs write identical bytes.
Standard library only; no network.
"""

import os
import shutil


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # Fail loudly on a partial copy instead of shipping a broken file.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
