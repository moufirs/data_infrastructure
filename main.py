from app.generator.generate import (
    batch,
    realtime,
)

from app.ingestion.ingest import main as ingest
from realtime.rabbitmq.producer import (
    start_producer,
)

from realtime.rabbitmq.consumer import (
    start_consumer,
)
from realtime.kafka.producer import (
    start_producer as start_kafka_producer,
)

from realtime.kafka.consumer import (
    start_consumer as start_kafka_consumer,
)

print()
print("1 - Batch Generator")
print("2 - Realtime Generator")
print("3 - Ingestion CSV")
print("4 - RabbitMQ Producer")
print("5 - RabbitMQ Consumer")
print("6 - Kafka Producer")
print("7 - Kafka Consumer")

choice = input("Choix : ")

if choice == "1":
    batch()

elif choice == "2":
    realtime()

elif choice == "3":
    ingest()

elif choice == "4":
    start_producer()

elif choice == "5":
    start_consumer()

elif choice == "6":

    start_kafka_producer()


elif choice == "7":

    start_kafka_consumer()

else:
    print("Choix invalide")