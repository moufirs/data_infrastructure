from app.storage.storage_interface import (
    StorageInterface,
)


class OzoneStorage(StorageInterface):

    def write(
        self,
        dataframe,
        layer,
        filename,
    ):
        raise NotImplementedError(
            "Apache Ozone sera implémenté plus tard."
        )