from uuid import UUID

from pydantic import BaseModel


class Notification(BaseModel):
    user_name: str
    user_last_name: str | None
    notification_body: str | None
    subject: str | None
    destanation: str
    additionnal_notification_data: str | None
