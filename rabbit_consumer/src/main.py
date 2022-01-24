import json
import logging

from core.settings import get_settings
from models.event import Event
from modules.exporter import get_exporter
from modules.rabbit import create_rabbitmq_connection

channel = create_rabbitmq_connection()
exporter = get_exporter()


def on_message(channel, method_frame, header_frame, body):
    event = Event(**json.loads(body)).dict()
    exporter.pass_message(event)
    logging.info("Event with ID {0} successfully passed".format(event["event_id"]))


def start():
    channel.basic_consume(on_message, queue=get_settings().rabbit_settings.queue_name)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception as ex:
        channel.stop_consuming()
        logging.error("RabbitMQ connection error: {0}".format(ex))


if __name__ == "__main__":
    pass
