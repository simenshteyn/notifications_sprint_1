from abc import ABC, abstractmethod

# from core.settings.core_settings import get_settings
from core.settings.notification_settings import SMSNotificationSettings
from models.notification import Notification
from services.notification.base_notification_service import BaseNotificationService


class SMSNotificationService(BaseNotificationService):
    def __init__(self, sms_notification_settings: SMSNotificationSettings, *args, **kwargs):
        pass

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
        print("Notifications has been sent")
        return True


# sms_notification_service = SMSNotificationService(
#     sms_notification_settings=get_settings().notification_settings.sms_settings
# )
