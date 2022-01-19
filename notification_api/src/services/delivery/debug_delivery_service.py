from models.notification import Notification
from services.delivery.base_delivery_service import BaseDeliveryService


class DebugDeliveryService(BaseDeliveryService):
    def __init__(self, *args, **kwargs):
        pass

    def send_notification(self, *, notification: Notification) -> bool:
        print("Sending.......")
        print(notification)
        print("Notification has been sent")
        return True

    def send_notifications(
        self,
        *,
        notifications: list[Notification] | tuple[Notification],
        notification_body: str | None = None,
    ) -> bool:
        print("Sending.......")
        print(notifications)
        print("Notification has been sent")
        return True
