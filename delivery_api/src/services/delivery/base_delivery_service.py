from abc import ABC, abstractmethod

from models.message import Message


class BaseDeliveryService(ABC):
    @abstractmethod
    async def send_notification(self, *, message: Message) -> bool:
        raise NotImplemented
