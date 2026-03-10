import pandas as pd
from pathlib import Path

# rutas
BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "processed" / "articles_labeled.csv"
output_dir = BASE_DIR / "tables"

# cargar datos
df = pd.read_csv(input_file)

# eliminar duplicados por DOI
df = df.drop_duplicates(subset="doi")

print("Total unique papers:", len(df))

# generar lista por label
labels = df["labels"].dropna().unique()

for label in labels:

    subset = df[df["labels"] == label]

    subset = subset[[
        "title",
        "year",
        "journal",
        "authors",
        "doi"
    ]]

    filename = output_dir / f"papers_{label}.csv"

    subset.to_csv(filename, index=False)

    print(f"{label}: {len(subset)} papers")

print("Reading lists generated.")