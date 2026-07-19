from app.storage.minio.minio_storage import (
    MinIOStorage,
)


storage = MinIOStorage()


if storage.is_connected():

    print("Connexion réussie.")

else:

    print("Connexion échouée.")