import asyncio
import logging
from abc import ABC, abstractmethod
from email.mime.text import MIMEText

from aiosmtplib import SMTP, SMTPException

from core.settings.delivery_settings import EmailDeliverySettings
from models.notification import Notification
from services.delivery.base_delivery_service import BaseDeliveryService

logger = logging.getLogger("notification_api")


class EmailDeliveryService(BaseDeliveryService):
    def __init__(
        self, *, email_notification_settings: EmailDeliverySettings, event_loop: asyncio.AbstractEventLoop
    ):
        self.email_notification_settings = email_notification_settings
        logger.debug("EmailNotificationService loaded with settings:")
        logger.debug(email_notification_settings)
        self.event_loop: asyncio.AbstractEventLoop = event_loop

    async def _send_with_send_message(self, message) -> None:
        smtp_client = SMTP(
            hostname=self.email_notification_settings.smtp_server,
            port=self.email_notification_settings.smtp_port,
            password=self.email_notification_settings.smtp_password,
            use_tls=self.email_notification_settings.use_tls,
        )
        await smtp_client.connect()
        await smtp_client.send_message(message)
        await smtp_client.quit()

    async def send_notification(self, *, notification: Notification) -> bool:
        mime_message = MIMEText(notification.notification_body)
        mime_message["From"] = self.email_notification_settings.smtp_user
        mime_message["To"] = notification.destanation
        mime_message["Subject"] = notification.subject
        try:
            await self._send_with_send_message(mime_message)
            return True
        except SMTPException as ex:
            logger.exception(ex)
            return False
