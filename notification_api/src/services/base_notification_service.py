from abc import ABC, abstractmethod

from models.notification import Notification


class BaseNotificationService(ABC):
    @abstractmethod
    def send_notification(self, notification: Notification):
        pass

    @abstractmethod
    def send_notifications(
        self,
        notifications: list[Notification] | tuple[Notification],
        notification_body: str | None = None,
    ):
        pass
