from app.ingestion.readers.csv_reader import CSVReader
from app.datalake.bronze.bronze_writer import BronzeWriter
from app.shared.logger import logger
from app.quality.structural.validation_service import (
    ValidationService,
)


class IngestionService:

    def ingest_csv(self, path):

        try:

            df = CSVReader.read(path)

            logger.info("CSV chargé")

            df = ValidationService.validate(df)

            BronzeWriter().write(df)

            return df

        except Exception:

            logger.exception("Le pipeline d'ingestion a échoué")

            raise