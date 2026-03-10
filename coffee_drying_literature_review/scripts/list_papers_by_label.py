import pandas as pd
from pathlib import Path
import sys

# ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

file_path = BASE_DIR / "data" / "processed" / "articles_labeled.csv"

# leer datos
df = pd.read_csv(file_path)

# verificar argumento
if len(sys.argv) < 2:
    print("Usage: python list_papers_by_label.py <label>")
    exit()

label = sys.argv[1]

# filtrar por label
subset = df[df["labels"] == label]

if subset.empty:
    print(f"No papers found for label: {label}")
    exit()

subset = subset.sort_values("year", ascending=False)

print(f"\nPapers for label: {label}")
print(f"Total: {len(subset)}\n")

for i, row in subset.iterrows():
    title = row["title"]
    authors = row["authors"]
    year = row["year"]

    print(f"{year} | {authors}")
    print(title)
    print("-" * 80)