from abc import ABC, abstractmethod
from uuid import UUID

from models.message import Message


class BaseMessageService(ABC):
    @abstractmethod
    async def get_message(self, *, event_id: UUID, user_id: UUID, template_id: UUID) -> Message | None:
        raise NotImplemented
