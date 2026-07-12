from app.generator.generators.batch_generator import BatchGenerator
from app.generator.generators.realtime_generator import RealtimeGenerator

from app.generator.exporters.csv_exporter import CSVExporter
from app.generator.exporters.parquet_exporter import ParquetExporter

from app.generator.config.settings import (
    CSV_FILE,
    PARQUET_FILE,
    NUMBER_OF_RECORDS,
)


def batch():

    generator = BatchGenerator()

    declarations = generator.generate(NUMBER_OF_RECORDS)

    CSVExporter.export(
        declarations,
        CSV_FILE,
    )

    ParquetExporter.export(
        declarations,
        PARQUET_FILE,
    )

    print(f"{len(declarations)} déclarations générées.")


def realtime():

    generator = RealtimeGenerator()

    generator.start()