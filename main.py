from app.generator.generate import (
    batch,
    realtime,
)

from app.ingestion.ingest import main as ingest


print()
print("1 - Batch Generator")
print("2 - Realtime Generator")
print("3 - Ingestion CSV")

choice = input("Choix : ")

if choice == "1":
    batch()

elif choice == "2":
    realtime()

elif choice == "3":
    ingest()

else:
    print("Choix invalide")