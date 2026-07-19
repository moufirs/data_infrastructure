from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


# BASE PROJECT
BASE_DIR = Path(__file__).resolve().parents[3]


# GENERATOR
DATASET_DIR = BASE_DIR / "app" / "generator" / "datasets"

CSV_FILE = DATASET_DIR / "declarations.csv"

PARQUET_FILE = DATASET_DIR / "declarations.parquet"

NUMBER_OF_RECORDS = 2000


# STORAGE
STORAGE_PATH = BASE_DIR / os.getenv("STORAGE_PATH", "storage")

BRONZE_LAYER = os.getenv("BRONZE_LAYER", "bronze")

SILVER_LAYER = os.getenv("SILVER_LAYER", "silver")

GOLD_LAYER = os.getenv("GOLD_LAYER", "gold")

FILE_FORMAT = os.getenv("FILE_FORMAT", "parquet")

# LOGGING
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


# MINIO
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")

MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")

MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")

MINIO_SECURE = os.getenv("MINIO_SECURE", "False") == "True"

BRONZE_BUCKET = os.getenv("BRONZE_BUCKET")

SILVER_BUCKET = os.getenv("SILVER_BUCKET")

GOLD_BUCKET = os.getenv("GOLD_BUCKET")


# RABBITMQ
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")

RABBITMQ_PORT = int(
    os.getenv(
        "RABBITMQ_PORT",
        5672
    )
)

RABBITMQ_USER = os.getenv(
    "RABBITMQ_USER"
)

RABBITMQ_PASSWORD = os.getenv(
    "RABBITMQ_PASSWORD"
)

RABBITMQ_QUEUE = os.getenv(
    "RABBITMQ_QUEUE"
)

# REALTIME
REALTIME_BUFFER_SIZE = int(
    os.getenv(
        "REALTIME_BUFFER_SIZE",
        10,
    )
)


# KAFKA
KAFKA_HOST = os.getenv(
    "KAFKA_HOST"
)

KAFKA_PORT = int(
    os.getenv(
        "KAFKA_PORT",
        9092,
    )
)

KAFKA_TOPIC = os.getenv(
    "KAFKA_TOPIC"
)