import uuid

import pika
from pydantic import BaseSettings, Field

from operators.models.event import Event


class NotificationSender:
    def __init__(self):
        self.host: str = Field("http://localhost:8001", env="MESSAGE_HOST")
        self.endpoint: str = Field("/api/v1/message/user", env="MESSAGE_ENDPOINT")
        self.notifications_file = Field("/tmp/notification", env="NOTIFICATIONS_FILE")
        self.template_endpoint: str = Field(
            "http://localhost:8001/api/v1/template/birthdate", env="TEMPLATE_ENDPOINT"
        )
        self.credentials = pika.PlainCredentials("guest", "guest")
        self.parameters = pika.ConnectionParameters("localhost", credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)

    def send_notifications(self):
        template_id: str = requests.get(self.template_endpoint)
        with open(self.notifications_file, encoding="utf8") as file:
            ids = file.readlines()
        event_id: uuid.UUID = uuid.uuid4()
        events: List[Event] = []
        for user_id in ids:
            events.append(
                Event(event_id=event_id, user_id=user_id, delivery_type="email", template_id=template_id)
            )
