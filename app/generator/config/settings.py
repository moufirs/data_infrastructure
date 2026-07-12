from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

DATASET_DIR = BASE_DIR / "app" / "generator" / "datasets"

CSV_FILE = DATASET_DIR / "declarations.csv"

PARQUET_FILE = DATASET_DIR / "declarations.parquet"

NUMBER_OF_RECORDS = 2000