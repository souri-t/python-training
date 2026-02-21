import csv
from pathlib import Path


def read_csv(file_path: str) -> list[list[str]]:
    """CSV ファイルのパスを受け取り、行データの配列を返す。"""
    path = Path(file_path)
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        return list(reader)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("使い方: python csv_reader.py <CSVファイルパス>")
        sys.exit(1)

    rows = read_csv(sys.argv[1])
    for row in rows:
        print(row)
