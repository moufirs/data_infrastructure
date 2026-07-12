from pathlib import Path

import pandas as pd


class CSVReader:

    @staticmethod
    def read(csv_file: Path) -> pd.DataFrame:

        if not csv_file.exists():
            raise FileNotFoundError(csv_file)

        return pd.read_csv(csv_file)