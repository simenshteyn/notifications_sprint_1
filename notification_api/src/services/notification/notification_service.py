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
    def __init__(self, *args, **kwargs) -> None:
        self.template_service = kwargs["template_service"]
        self.logger = kwargs["logger"]

    async def get_notification(self, *, user: User, event: Event) -> Notification | None:
        self.logger.debug(user)
        self.logger.debug(event)

        destanation = user.email

        notification_body = await self.template_service.get_message_body(
            template_id=event.template_id, user=user
        )
        notification_body = "notification_body"
        notification: Notification = Notification(
            user_name=user.user_name,
            user_last_name=user.user_last_name,
            notification_body=notification_body,
            subject=event.subject,
            destanation=user.email,
        )
        return notification
