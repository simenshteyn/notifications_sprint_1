from abc import ABC, abstractmethod

from models.notification import Notification


class BaseDeliveryService(ABC):
    @abstractmethod
    async def send_notification(self, *, notification: Notification) -> bool:
        raise NotImplemented
