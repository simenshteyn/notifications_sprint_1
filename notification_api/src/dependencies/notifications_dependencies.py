from services.notification import (
    DebugNotificationService,
    EmailNotificationService,
    SMSNotificationService,
)
from services.user import BaseUserService

user_service: BaseUserService | None = None


def get_user_service() -> BaseUserService | None:
    return user_service() if user_service else None


email_notification_service: EmailNotificationService | None = None


def get_email_notification_service() -> EmailNotificationService | None:
    return email_notification_service() if email_notification_service else None


sms_notification_service: SMSNotificationService | None = None


def get_sms_email_notification_service() -> SMSNotificationService | None:
    return sms_notification_service() if sms_notification_service else None


debug_notification_service: DebugNotificationService | None = None


def get_debug_email_notification_service() -> DebugNotificationService | None:
    return debug_notification_service() if debug_notification_service else None
