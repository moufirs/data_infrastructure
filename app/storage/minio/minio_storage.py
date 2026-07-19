from io import BytesIO
from datetime import datetime
import pandas as pd
from minio import Minio

from app.config.settings import (
    MINIO_ENDPOINT,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY,
    MINIO_SECURE,
)

from app.shared.logger import logger
from app.storage.storage_interface import StorageInterface


class MinIOStorage(StorageInterface):

    def __init__(self):

        self.client = Minio(
            endpoint=MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=MINIO_SECURE,
        )


    def write(
            self,
            dataframe: pd.DataFrame,
            layer: str,
            filename: str,
    ):

        try:

            if not self.client.bucket_exists(layer):

                self.client.make_bucket(layer)


            buffer = BytesIO()

            dataframe.to_parquet(
                buffer,
                index=False,
            )

            buffer.seek(0)

            today = datetime.now()
            object_name = (

                f"{today.year}/"

                f"{today.month:02}/"

                f"{today.day:02}/"

                f"{filename}"

            )
            
            self.client.put_object(

                bucket_name=layer,

                object_name=object_name,

                data=buffer,

                length=len(buffer.getvalue()),

                content_type="application/octet-stream",

            )


            logger.info(
                f"{filename} envoyé dans le bucket '{layer}'."
            )


        except Exception as e:

            logger.exception(
                f"Erreur MinIO : {e}"
            )

            raise