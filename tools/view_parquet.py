import pandas as pd

df = pd.read_parquet(
    "storage/bronze/2026/07/13/declarations.parquet"
)

print(df.head(20))