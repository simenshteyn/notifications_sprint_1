from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from models.notification import Notification
from models.user import User


class BaseUserService(ABC):
    @abstractmethod
    def get_private_user_data(self, *, user_id: UUID) -> User | None:
        raise NotImplemented
