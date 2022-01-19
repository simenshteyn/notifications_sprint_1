from abc import ABC, abstractmethod
from uuid import UUID

from models.event import Event
from models.notification import Notification
from models.user import User
from services.template.base_template_service import BaseTemplateService


class BaseNotificationService(ABC):
    @abstractmethod
    def __init__(self, *, template_service: BaseTemplateService) -> None:
        pass

    @abstractmethod
    def get_notification(self, *, event: Event) -> Notification | None:
        pass

    @abstractmethod
    def get_notifications(self, *, events: list[Event]) -> tuple[Notification] | None:
        pass
