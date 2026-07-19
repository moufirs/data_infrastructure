import json
import pika
import pandas as pd
from app.quality.structural.validation_service import ValidationService
from app.datalake.bronze.bronze_writer import BronzeWriter
from app.config.settings import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
    RABBITMQ_QUEUE,
)

from app.config.settings import (
    REALTIME_BUFFER_SIZE,
)

from app.quality.structural.validation_service import (
    ValidationService,
)

from app.datalake.bronze.bronze_writer import (
    BronzeWriter,
)

from realtime.realtime_service import (
    RealtimeService,
)

buffer = []
realtime_service = RealtimeService()

def callback(
        ch,
        method,
        properties,
        body,
):

    declaration = json.loads(
        body.decode()
    )

    print(

        f"Déclaration reçue : "

        f"{declaration['numero_dum']}"

    )

    realtime_service.process(
        declaration
    )

def start_consumer():

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


    channel.basic_consume(

        queue=RABBITMQ_QUEUE,

        on_message_callback=callback,

        auto_ack=True,

    )


    print(
        "Consumer Started ..."
    )


    channel.start_consuming()