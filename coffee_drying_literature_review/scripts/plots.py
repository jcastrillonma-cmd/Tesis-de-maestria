import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/articles_labeled_leather.csv")

# artículos por label
label_counts = df["labels"].value_counts()

plt.figure()
label_counts.plot(kind="bar")
plt.ylabel("Number of papers")
plt.title("Distribution of papers by topic")

plt.tight_layout()
plt.savefig("../figures/papers_per_label.png")

# artículos por año
year_counts = df["year"].value_counts().sort_index()

plt.figure()
year_counts.plot(kind="bar")
plt.ylabel("Number of papers")
plt.title("Publications per year")

plt.tight_layout()
plt.savefig("../figures/papers_per_year.png")

print("Figuras guardadas en figures/")