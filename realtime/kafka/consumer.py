import json

from kafka import KafkaConsumer

from app.config.settings import (
    KAFKA_HOST,
    KAFKA_PORT,
    KAFKA_TOPIC,
)

from realtime.realtime_service import (
    RealtimeService,
)


def start_consumer():

    realtime_service = RealtimeService()

    consumer = KafkaConsumer(

        KAFKA_TOPIC,

        bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}",

        auto_offset_reset="earliest",

        value_deserializer=lambda value:
        json.loads(
            value.decode("utf-8")
        ),

    )

    print()
    print("Kafka Consumer Started ...")
    print()

    for message in consumer:

        declaration = message.value

        realtime_service.process(
            declaration
        )