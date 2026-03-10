# Coffee Drying Literature Review

## Overview

This repository contains the datasets and scripts used for the literature review related to coffee drying technologies, drying kinetics, energy efficiency, and their effects on coffee quality.

The literature screening and labeling process was conducted using Rayyan. The repository includes scripts to extract labels and organize the literature database for analysis and thesis writing.

This work supports the development of a master's thesis focused on the analysis and design of coffee drying systems.

---

## Repository Structure

```
coffee-drying-literature-review
│
├── data
│   ├── raw
│   │   └── articles_rayyan.csv
│   │
│   └── processed
│       └── articles_labeled.csv
│
├── scripts
│   └── extract_rayyan_labels.py
│
├── notebooks
│   └── literature_analysis.ipynb
│
├── figures
│   ├── papers_per_year.png
│   ├── papers_per_label.png
│
├── tables
│   └── literature_matrix.xlsx
│
└── README.md
```

---

## Data Sources

The bibliographic data was obtained from academic databases and exported from Rayyan after the screening and labeling process.

The dataset contains information such as:

* Title
* Authors
* Year
* Journal
* DOI
* Abstract
* Keywords
* Custom labels used to categorize the literature

---

## Literature Labels

The articles were classified using the following thematic labels:

* coffee_general
* coffee_processing
* coffee_drying_stage
* drying_kinetics
* solar_drying
* mechanical_drying
* heat_pump_drying
* energy_efficiency
* dryer_design
* coffee_quality

These labels correspond to the thematic structure used for the theoretical framework of the thesis.

---

## Scripts

### extract_rayyan_labels.py

This script processes the exported Rayyan dataset and extracts the custom labels stored inside the `notes` field. The script generates a clean dataset where each article is associated with its respective thematic labels.

---

## Analysis

The processed dataset can be used to:

* group articles by research topic
* analyze publication trends
* identify key research areas in coffee drying
* support the construction of the thesis theoretical framework

---

## License

This repository only contains bibliographic metadata and analysis scripts. Full articles are not included due to copyright restrictions.

---

## Author

Master's student working on coffee drying technologies and energy efficiency in post-harvest coffee processing.
