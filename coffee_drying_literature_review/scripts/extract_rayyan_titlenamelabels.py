import pandas as pd
import re

# cargar datos
df = pd.read_csv("../data/raw/articles_leather.csv")

# función para extraer labels
def extract_labels(text):
    if pd.isna(text):
        return []
    
    match = re.search(r'RAYYAN-LABELS:\s*(.*)', str(text))
    
    if match:
        labels = match.group(1)
        return [l.strip() for l in labels.split(",")]
    
    return []

# crear columna labels
df["labels"] = df["notes"].apply(extract_labels)

# expandir filas (una fila por label)
df = df.explode("labels")

# seleccionar SOLO columnas necesarias
df_clean = df[[
    "title",
    "doi",
    "labels"
]]

# eliminar filas sin label (opcional pero recomendado)
df_clean = df_clean.dropna(subset=["labels"])

# guardar base limpia
df_clean.to_csv("../data/processed/articles_labeled_leather_titledoilabbel.csv", index=False)

print("Archivo generado en data/processed/")