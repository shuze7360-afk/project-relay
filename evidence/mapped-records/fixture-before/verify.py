import csv
from pathlib import Path
base = Path(__file__).resolve().parent
with (base / 'data.csv').open(encoding='utf-8', newline='') as stream:
    expected = sum(int(row['value']) for row in csv.DictReader(stream))
actual = int((base / 'report.txt').read_text(encoding='utf-8').strip())
print(f'expected={expected} actual={actual}')
raise SystemExit(0 if expected == actual else 1)
