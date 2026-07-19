from pathlib import Path

import pandas as pd


class CSVReader:

    @staticmethod
    def read(csv_file: Path) -> pd.DataFrame:

        if not csv_file.exists():
            raise FileNotFoundError(csv_file)
        try:
            return pd.read_csv(
                csv_file,
                parse_dates=["date_depot"],
                dtype={
                    "declaration_id": str,
                    "numero_dum": str,
                    "bureau_enregistrement": str,
                    "code_regime": str,
                    "exportateur": str,
                    "importateur": str,
                    "declarant": str,
                    "pays_provenance": str,
                    "pays_origine": str,
                    "pays_destination": str,
                    "conditions_livraison": str,
                    "devise": str,
                    "code_marchandise": str,
                    "designation_marchandise": str,
                    "mode_transport": str,
                }
            )
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la lecture du CSV : {e}")
        