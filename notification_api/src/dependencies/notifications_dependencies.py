from core.settings.core_settings import get_settings
from services.notification import (
    BaseNotificationService,
    DebugNotificationService,
    EmailNotificationService,
    SMSNotificationService,
)

notification_services: dict[BaseNotificationService, str] = {}


def get_email_notification_services() -> dict[BaseNotificationService, str] | None:
    return notification_services
