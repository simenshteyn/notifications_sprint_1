from functools import lru_cache
from uuid import UUID

from fastapi import Depends

from dependencies.template_dependencies import get_end_point_template_service
from models.event import Event
from models.notification import Notification
from models.user import User
from services.notification.base_notification_service import BaseNotificationService
from services.template.base_template_service import BaseTemplateService


class NotificationService(BaseNotificationService):
    def __init__(self, *, template_service: BaseTemplateService) -> None:
        self.template_service = template_service

    def get_notification(self, *, event: Event) -> Notification | None:
        pass

    def get_notifications(self, *, events: list[Event]) -> tuple[Notification] | None:
        pass


@lru_cache()
def get_notification_service(
    template_service: BaseTemplateService = Depends(get_end_point_template_service),
) -> NotificationService:
    return NotificationService(template_service=template_service)
