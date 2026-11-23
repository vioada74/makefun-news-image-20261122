#!/usr/bin/env python3
"""Salin gambar entri berita ke direktori keluaran make.fun.

Gambar yang disalin adalah koran satu halaman yang merangkum berita dunia
pada Minggu, 22 November 2026: berita utama COP31 yang runtuh, tujuh blok
foto berita lain, dan sebuah ticker di bagian bawah. Gambar itu sudah jadi
sebelum program ini dijalankan; tugas program ini hanyalah memindahkannya
ke tempat yang diminta make.fun, tanpa mengubah satu byte pun.

Karena penyalinan dilakukan byte demi byte dan tidak ada waktu, angka acak,
atau masukan lain yang ikut tertulis ke hasil, menjalankan program ini dua
kali dengan sumber yang sama selalu menghasilkan file yang byte-nya
identik. Itulah yang membuat hasil build dapat direproduksi.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    if not os.path.isfile(source):
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1
    if os.path.getsize(source) == 0:
        print(f"error: source image is empty: {source}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, SOURCE_NAME)

    shutil.copyfile(source, target)

    if os.path.getsize(target) != os.path.getsize(source):
        print(
            f"error: copied file size {os.path.getsize(target)} does not "
            f"match source size {os.path.getsize(source)}",
            file=sys.stderr,
        )
        return 1

    print(f"copied {source} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
