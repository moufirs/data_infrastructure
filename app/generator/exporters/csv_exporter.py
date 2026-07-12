from dataclasses import asdict
from pathlib import Path

import pandas as pd

from app.generator.models.declaration import DeclarationDUM


class CSVExporter:

    @staticmethod
    def export(
        declarations: list[DeclarationDUM],
        output_file: Path,
    ) -> None:

        rows = [
            asdict(declaration)
            for declaration in declarations
        ]

        df = pd.DataFrame(rows)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_csv(
            output_file,
            index=False,
            encoding="utf-8-sig",
        )

        print(f"CSV créé : {output_file}")