import logging
from functools import lru_cache

import requests

from core.settings import get_settings
from models.event import Event


class MessageExporter:
    def __init__(self):
        base = self.get_base_url() + "/api/{0}"

    def get_base_url(self):
        return f"{get_settings().delivery_settings.host}:{get_settings().delivery_settings.port}"

    def pass_message(self, event: Event):
        url = self.base.format("send/")
        result = {}
        try:
            result = requests.post(url, event.json())
        except Exception as ex:
            logging.error("Got exception while passing event: {0}".format(ex))

        return result


@lru_cache
def get_exporter() -> MessageExporter:
    exporter = MessageExporter()
    return exporter
