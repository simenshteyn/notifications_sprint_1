from abc import ABC, abstractmethod

# from core.settings.core_settings import get_settings
from core.settings.notification_settings import EmailNotificationSettings
from models.notification import Notification
from services.notification.base_notification_service import BaseNotificationService


class EmailNotificationService(BaseNotificationService):
    def __init__(self, email_notification_settings: EmailNotificationSettings, *args, **kwargs):
        self.email_notification_settings = email_notification_settings

    def send_notification(self, notification: Notification) -> bool:
        print("Sending.......")
        print(notification)
        print("Notification has been sent")
        return True

    def send_notifications(
        self,
        notifications: list[Notification] | tuple[Notification],
        notification_body: str | None = None,
    ) -> bool:
        print("Sending.......")
        print(notifications)
        print("Notification has been sent")
        return True


# email_notification_service = EmailNotificationService(
#     email_notification_settings=get_settings().notification_settings.email_settings
# )
