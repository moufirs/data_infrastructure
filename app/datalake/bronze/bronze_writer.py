from app.storage.local.local_storage import LocalStorage
from app.storage.minio.minio_storage import MinIOStorage
from app.utils.file_utils import FileUtils
from app.shared.logger import logger

class BronzeWriter:

    def __init__(self):
        self.storage = MinIOStorage()

    def write(self, dataframe):

        try:

            filename = FileUtils.generate_filename()

            self.storage.write(
                dataframe=dataframe,
                layer="bronze",
                filename=filename,
            )

            logger.info("Écriture Bronze terminée")

        except Exception:

            logger.exception("Erreur pendant l'écriture Bronze")

            raise