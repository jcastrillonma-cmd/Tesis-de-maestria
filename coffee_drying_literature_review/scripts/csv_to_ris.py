import pandas as pd

# Cargar datos
df = pd.read_csv("../data/processed/articles_labeled.csv")

# Función para convertir a formato RIS
def to_ris(row):
    ris_entry = ""

    # Tipo de documento
    ris_entry += "TY  - JOUR\n"

    # Título
    if pd.notna(row.get("title")):
        ris_entry += f"TI  - {row['title']}\n"

    # Autores (separados por ;)
    if pd.notna(row.get("authors")):
        authors = str(row["authors"]).split(";")
        for author in authors:
            ris_entry += f"AU  - {author.strip()}\n"

    # Año
    if pd.notna(row.get("year")):
        ris_entry += f"PY  - {int(row['year'])}\n"

    # Revista
    if pd.notna(row.get("journal")):
        ris_entry += f"JO  - {row['journal']}\n"

    # DOI
    if pd.notna(row.get("doi")):
        ris_entry += f"DO  - {row['doi']}\n"

    # Keywords
    if pd.notna(row.get("keywords")):
        keywords = str(row["keywords"]).split(";")
        for kw in keywords:
            ris_entry += f"KW  - {kw.strip()}\n"

    # Fin de registro
    ris_entry += "ER  - \n\n"

    return ris_entry

# Convertir todo
ris_text = "".join(df.apply(to_ris, axis=1))

# Guardar archivo
with open("../data/processed/vosviewer_input.ris", "w", encoding="utf-8") as f:
    f.write(ris_text)

print("Archivo RIS generado para VOSviewer")