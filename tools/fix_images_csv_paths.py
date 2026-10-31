"""Write a portable copy of artifacts/tables/images.csv (path_rgb with '/').

Usage (from the repository root):
    python tools/fix_images_csv_paths.py [output_path]

The frozen original is only read, never modified. Default output:
patches/images.csv
"""
import csv
import sys
from pathlib import Path

SRC = Path("artifacts/tables/images.csv")
DST = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("patches/images.csv")


def main():
    with open(SRC, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    col = rows[0].index("path_rgb")
    for row in rows[1:]:
        row[col] = row[col].replace("\\", "/")
    DST.parent.mkdir(parents=True, exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)
    print(f"wrote {DST} ({len(rows) - 1} rows)")


if __name__ == "__main__":
    main()
