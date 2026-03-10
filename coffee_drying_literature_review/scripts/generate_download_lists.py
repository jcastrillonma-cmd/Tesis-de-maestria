import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "processed" / "articles_labeled.csv"
output_dir = BASE_DIR / "tables"

output_dir.mkdir(exist_ok=True)

df = pd.read_csv(input_file)

# eliminar duplicados globales por DOI
df_unique = df.drop_duplicates(subset="doi")

# detectar artículos repetidos en diferentes labels
duplicate_titles = df_unique["title"][df_unique["title"].duplicated(keep=False)]

df_unique["appears_in_multiple_labels"] = df_unique["title"].isin(duplicate_titles)

# columna para marcar si ya descargaste el paper
df_unique["downloaded"] = "no"

# seleccionar columnas útiles
df_unique = df_unique[[
    "title",
    "authors",
    "year",
    "journal",
    "doi",
    "labels",
    "appears_in_multiple_labels",
    "downloaded"
]]

# guardar archivo maestro
master_file = output_dir / "all_papers_download_list.csv"
df_unique.to_csv(master_file, index=False)

print("Master download list created")

# generar archivos por label
labels = df_unique["labels"].dropna().unique()

for label in labels:

    subset = df_unique[df_unique["labels"] == label]

    filename = output_dir / f"download_list_{label}.csv"

    subset.to_csv(filename, index=False)

    print(f"{label}: {len(subset)} papers")

print("Download lists generated")