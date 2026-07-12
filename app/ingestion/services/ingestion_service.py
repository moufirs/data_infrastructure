import pandas as pd

from app.ingestion.readers.csv_reader import CSVReader


class IngestionService:

    def ingest_csv(self, csv_path):

        df = CSVReader.read(csv_path)

        print(f"{len(df)} lignes chargées.")

        return df