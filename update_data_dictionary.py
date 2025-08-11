# === Install dependencies ===
import pandas as pd
import os
import requests
import yaml
from pathlib import Path

# === Configuration === 
USE_LOCAL = os.getenv("USE_LOCAL", "true").lower() == "true" #this is default
LOCAL_CSV = "GP2_Data_Dictionary_ver1.1.csv"
CSV_URL = os.getenv("CSV_URL") #to switch to published Google Sheet (live doc)

OUTPUT_CSV = "data_dictionary.csv"
OUTPUT_YAML = "data_dictionary.yaml"
DOCS_DIR = Path("docs")
BASE_YML = Path("mkdocs.base.yml")
FINAL_YML = Path("mkdocs.yml")
CATEGORY_COLUMN = "Modality"
DROP_COLUMNS = ["Comment", "Cat", "Single measure", "reviewed", "no", "AMP_PD_item", "conversion"]

CUSTOM_ORDER = ["Base", "Demographics", "Family history", "Known_relatedness", "Diagnosis", "MDS_Diagnostic_criteria", "PD History", "Medical History", "Clinical diagnosis of complications", "Current Medication Status", "Vitals", "Lifestyle",  "CISI-PD", "Hoehn and Yahr", "Rankin Scale", "MDS UPDRS Part I", "MDS UPDRS Part II", "MDS UPDRS Part III", " MDS UPDRS Part IV", "UPDRS Part I", "UPDRS Part II", "UPDRS Part III", "UPDRS Part IV", "MoCA", "MMSE", "SCOPA-COG", "SCOPA-AUT", "RBD DIagnosis", "RBD Screening Questionnaire", "RBD Single-Question Screen", "Epworth Sleepiness Scale", "Geriatric Depression Scale", "Orthostatic hypotension", "Scwab England ADL", "Olfactory test", "Misc Depression Scale", "PDQ-39", "WBC counts", "King's PD pain scale", "Modified MERQ-PD", "MERQ-PD-B", "DAT_imaging", "MIBG_imaging", "Pathology", "SAA Positivity", "Availability", "MDS-MSA", "MDS-PSP", "CBS-Armstrong", "DLB", "UMSARS part I", "UMSARS part II", "UMSARS part III", "UMSARS part IV", "CBFS B", "PSP-CDS", "PSP-RS part I", "PSP-RS part II", "PSP-RS part III", "PSP-RS part IV", "PSP-RS Part V", "PSP-RS part VI", "PSP-RS", "IDEA Screening Questionnaire"]

# === Load data ===
if USE_LOCAL:
    print(f"Reading local csv: {LOCAL_CSV}")
    df = pd.read_csv(LOCAL_CSV)
else:
    if not CSV_URL:
        raise ValueError("CSV_URL muste be set when USE_LOCAL is false.")
    print("Downloading google sheet csv!")
    resp = requests.get(CSV_URL)
    raw_path = "_raw_data_dictionary.csv"
    with open(raw_path, "wb") as f:
        f.write(resp.content)
    df = pd.read_csv(raw_path)

# === Clean data ===
df_clean = df.drop(columns=[c for c in DROP_COLUMNS if c in df.columns], errors="ignore")

# Save cleaned csv + yaml
df_clean.to_csv(OUTPUT_CSV, index=False)
with open(OUTPUT_YAML, "w") as f:
    yaml.safe_dump(df_clean.to_dict(orient="records"), f)

# === Build MkDocs pages ===
(DOCS_DIR / "modalities").mkdir(parents=True, exist_ok=True)

# Index page
index_lines = [
    "# Data Dictionary",
    "",
    "This is the current public version of the data dictionary grouped by modality.",
    "",
    "Use the search box for a quick search of variables."
]
(DOCS_DIR / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

# Order of appearance for categories
if CATEGORY_COLUMN in df_clean.columns:
    categories = sorted(
        df_clean[CATEGORY_COLUMN].dropna().unique(),
        key=lambda x: (CUSTOM_ORDER.index(x) if x in CUSTOM_ORDER else len(CUSTOM_ORDER) + hash(x))
    )
    for category in categories:
        group_df = df_clean[df_clean[CATEGORY_COLUMN] == category]
        page_lines = [f"# {category}", "", group_df.to_markdown(index=False)]
        (DOCS_DIR / "modalities" / f"{category}.md").write_text("\n".join(page_lines), encoding="utf-8")
else:
    categories = []

# === Dynamically generate mkdocs.yml ===
with open(BASE_YML) as f:
    base_config = yaml.safe_load(f)

nav = [{"Home": "index.md"}]
if categories:
    nav.append({"Modalities": [{cat: f"modalities/{cat}.md"} for cat in categories]})
base_config["nav"] = nav

with open(FINAL_YML, "w") as f:
    yaml.safe_dump(base_config, f, sort_keys=False)

print(f"MkDocs documentation and navigation has been updated (mode: {'local' if USE_LOCAL else 'Google Sheets'}).")