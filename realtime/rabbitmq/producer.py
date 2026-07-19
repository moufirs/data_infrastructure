import json
import random
import time
from dataclasses import asdict

import pika

from app.config.settings import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
    RABBITMQ_QUEUE,
)

from app.generator.generators.realtime_generator import (
    RealtimeGenerator,
)


def start_producer():

    credentials = pika.PlainCredentials(
        RABBITMQ_USER,
        RABBITMQ_PASSWORD,
    )

    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials,
    )

    connection = pika.BlockingConnection(
        parameters
    )

    channel = connection.channel()

    channel.queue_declare(
        queue=RABBITMQ_QUEUE,
    )

    generator = RealtimeGenerator()

    print("RabbitMQ Producer Started ...")

    while True:

        declaration = generator.generate()

        message = json.dumps(
            asdict(declaration),
            default=str,
        )

        channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_QUEUE,
            body=message,
        )

        print(
            f"Déclaration envoyée : {declaration.numero_dum}"
        )

        time.sleep(
            random.uniform(
                1,
                5,
            )
        )