from app.generator.config.settings import CSV_FILE

from app.ingestion.services.ingestion_service import (
    IngestionService,
)


def main():

    service = IngestionService()

    df = service.ingest_csv(CSV_FILE)

    print(df.head())


if __name__ == "__main__":
    main()