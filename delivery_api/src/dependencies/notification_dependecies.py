from functools import lru_cache

from core.settings.template_settings import EndpointTemplateServiceSettings
from services.notification.base_notification_service import BaseNotificationService

notification_service: BaseNotificationService | None = None


def set_notification_service(BaseNotificationService, *args, **kwargs) -> BaseNotificationService:
    return BaseNotificationService(*args, **kwargs)


@lru_cache
def get_notification_service() -> BaseNotificationService | None:
    return notification_service
