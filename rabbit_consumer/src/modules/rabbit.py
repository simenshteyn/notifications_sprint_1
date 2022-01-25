import logging

from pika import BlockingConnection, URLParameters

from core.settings import get_settings


def create_rabbitmq_connection():
    rabbit_settings = get_settings().rabbit_settings
    parameters = URLParameters(rabbit_settings.server_url)
    try:
        connection = BlockingConnection(parameters=parameters)
        channel = connection.channel()
        channel.queue_declare(rabbit_settings.queue_name, durable=True)
        logging.info("Connection success")
        return channel
    except Exception as ex:
        logging.error("Got exception while connecting RabbitMQ: {0}".format(ex))
