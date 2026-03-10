import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "processed" / "articles_labeled.csv"
output_dir = BASE_DIR / "tables"

output_dir.mkdir(exist_ok=True)

df = pd.read_csv(input_file)

# separar labels múltiples
df["labels"] = df["labels"].str.split(";")

# convertir cada label en una fila independiente
df = df.explode("labels")

df["labels"] = df["labels"].str.strip()

# eliminar duplicados reales por DOI
df_unique = df.drop_duplicates(subset=["doi", "labels"])

# marcar si aparece en múltiples labels
label_counts = df.groupby("doi")["labels"].nunique()

df_unique["appears_in_multiple_labels"] = df_unique["doi"].map(lambda x: label_counts[x] > 1)

df_unique["downloaded"] = "no"

columns = [
    "title",
    "authors",
    "year",
    "journal",
    "doi",
    "labels",
    "appears_in_multiple_labels",
    "downloaded"
]

df_unique = df_unique[columns]

# guardar lista maestra
master_file = output_dir / "all_papers_download_list.csv"
df_unique.to_csv(master_file, index=False)

print("Master download list created")

# generar lista por label
labels = sorted(df_unique["labels"].dropna().unique())

for label in labels:

    subset = df_unique[df_unique["labels"] == label]

    filename = output_dir / f"download_list_{label}.csv"

    subset.to_csv(filename, index=False)

    print(f"{label}: {len(subset)} papers")

print("Download lists generated")