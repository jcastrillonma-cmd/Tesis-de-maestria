import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# 📂 1. CARGAR DATOS
# ===============================

df = pd.read_csv("../data/processed/articles_labeled_leather.csv")

# ===============================
# 🧹 2. LIMPIAR Y SEPARAR LABELS
# ===============================

# Separar tipo y valor desde la columna labels
df[["tipo", "valor"]] = df["labels"].str.split(": ", expand=True)

# ===============================
# 🔄 3. CONVERTIR A FORMATO TABLA
# ===============================

df_pivot = df.pivot_table(
    index="title",
    columns="tipo",
    values="valor",
    aggfunc=lambda x: ", ".join(x.dropna().unique())
).reset_index()

# Quitar nombre de columnas
df_pivot.columns.name = None

# Renombrar columnas
df_pivot = df_pivot.rename(columns={
    "Residuos": "residuos",
    "Tipo de valorización": "valorizacion",
    "Producto": "producto"
})

# ===============================
# 💾 4. GUARDAR DATA LIMPIA
# ===============================

df_pivot.to_csv("../data/processed/articles_clean_leather.csv", index=False)

# ===============================
# 📊 5. DISTRIBUCIÓN POR RESIDUOS
# ===============================

residuos = df_pivot["residuos"].dropna().str.split(", ").explode()
residuos_counts = residuos.value_counts()

plt.figure()
residuos_counts.plot(kind="bar")
plt.ylabel("Número de artículos")
plt.title("Distribución por tipo de residuo")

plt.tight_layout()
plt.savefig("../figures/leather_residuos_dist.png")

# ===============================
# 📊 6. TIPOS DE VALORIZACIÓN
# ===============================

val = df_pivot["valorizacion"].dropna().str.split(", ").explode()
val_counts = val.value_counts()

plt.figure()
val_counts.plot(kind="bar")
plt.ylabel("Número de artículos")
plt.title("Tipos de valorización")

plt.tight_layout()
plt.savefig("../figures/leather_valorizacion_dist.png")

# ===============================
# 📊 7. TIPOS DE PRODUCTO
# ===============================

prod = df_pivot["producto"].dropna().str.split(", ").explode()
prod_counts = prod.value_counts()

plt.figure()
prod_counts.plot(kind="bar")
plt.ylabel("Número de artículos")
plt.title("Tipo de productos obtenidos")

plt.tight_layout()
plt.savefig("../figures/leather_productos_dist.png")

# ===============================
# 📊 8. MATRIZ RESIDUO vs PRODUCTO
# ===============================

df_matrix = df_pivot.copy()

# eliminar filas con NaN en estas columnas
df_matrix = df_matrix.dropna(subset=["residuos", "producto"])

# separar múltiples valores
df_matrix["residuos"] = df_matrix["residuos"].str.split(", ")
df_matrix["producto"] = df_matrix["producto"].str.split(", ")

# expandir combinaciones
df_matrix = df_matrix.explode("residuos").explode("producto")

# 🔥 MUY IMPORTANTE: resetear índice (evita tu error)
df_matrix = df_matrix.reset_index(drop=True)

# crear matriz
matrix = pd.crosstab(df_matrix["residuos"], df_matrix["producto"])

# graficar matriz
plt.figure(figsize=(8,6))
plt.imshow(matrix, aspect="auto")
plt.colorbar(label="Número de artículos")

plt.xticks(range(len(matrix.columns)), matrix.columns, rotation=45)
plt.yticks(range(len(matrix.index)), matrix.index)

plt.title("Matriz Residuo vs Producto")

plt.tight_layout()
plt.savefig("../figures/leather_matrix_residuo_producto.png")

# ===============================
# ✅ FINAL
# ===============================

print("✅ Script ejecutado correctamente")
print("📊 Figuras guardadas en /figures/")
print("📁 Dataset limpio guardado en /data/processed/")