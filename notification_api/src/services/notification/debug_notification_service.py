from models.notification import Notification
from services.notification.base_notification_service import BaseNotificationService


class DebugNotificationService(BaseNotificationService):
    def __init__(self, *args, **kwargs):
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
        print("Notification has been sent")
        return True


# debug_notification_service = DebugNotificationService()
