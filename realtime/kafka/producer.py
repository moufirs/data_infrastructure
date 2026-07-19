import json
import random
import time
from dataclasses import asdict

from kafka import KafkaProducer

from app.config.settings import (
    KAFKA_HOST,
    KAFKA_PORT,
    KAFKA_TOPIC,
)

from app.generator.generators.realtime_generator import (
    RealtimeGenerator,
)


def start_producer():

    producer = KafkaProducer(

        bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}",

        value_serializer=lambda value:
        json.dumps(
            value,
            default=str,
        ).encode(
            "utf-8"
        ),

    )

    generator = RealtimeGenerator()

    print()
    print("Kafka Producer Started ...")
    print()

    while True:

        declaration = generator.generate()

        producer.send(

            KAFKA_TOPIC,

            value=asdict(
                declaration
            ),

        )

        producer.flush()

        print(

            f"Déclaration envoyée : "
            f"{declaration.numero_dum}"

        )

        time.sleep(

            random.uniform(
                1,
                5,
            )

        )