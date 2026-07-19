from pathlib import Path
from datetime import datetime
import pandas as pd
from app.storage.storage_interface import StorageInterface
from app.shared.logger import logger


class LocalStorage(StorageInterface):

    def __init__(self):

        self.base_path = Path("storage")

    def write(
        self,
        dataframe: pd.DataFrame,
        layer: str,
        filename: str,
    ):

        today = datetime.now()

        path = (
            self.base_path
            / layer
            / str(today.year)
            / f"{today.month:02}"
            / f"{today.day:02}"
        )

        path.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_file = path / filename

        dataframe.to_parquet(
            output_file,
            index=False,
        )

        logger.info(f"Fichier enregistré : {output_file}")