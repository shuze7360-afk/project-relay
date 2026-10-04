"""clean — 读取 CSV，跳过空行后原样写回（未完成：重复行处理）。"""
import csv


def clean_rows(rows):
    out = []
    for r in rows:
        if any(str(c).strip() for c in r):
            out.append(r)
    return out


if __name__ == "__main__":
    import sys
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    with open(dst, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(clean_rows(rows))
