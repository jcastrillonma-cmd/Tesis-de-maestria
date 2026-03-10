import pandas as pd

df = pd.read_csv("../data/processed/articles_labeled.csv")

print("Artículos por tema:")

print(df["labels"].value_counts())

print("\nArtículos por año:")

print(df["year"].value_counts().sort_index())