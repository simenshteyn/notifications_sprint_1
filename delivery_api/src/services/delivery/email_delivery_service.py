import asyncio
import logging
from abc import ABC, abstractmethod
from email.mime.text import MIMEText

from aiosmtplib import SMTP, SMTPException

from core.settings.delivery_settings import EmailDeliverySettings
from models.message import Message
from services.delivery.base_delivery_service import BaseDeliveryService

logger = logging.getLogger("delivery_api")


class EmailDeliveryService(BaseDeliveryService):
    def __init__(
        self, *, email_delivery_settings: EmailDeliverySettings, event_loop: asyncio.AbstractEventLoop
    ):
        self.email_delivery_settings = email_delivery_settings
        logger.debug("EmailNotificationService loaded with settings:")
        logger.debug(self.email_delivery_settings)
        self.event_loop: asyncio.AbstractEventLoop = event_loop

    async def _send_with_send_message(self, mime_message) -> None:
        smtp_client = SMTP(
            hostname=self.email_delivery_settings.smtp_server,
            port=self.email_delivery_settings.smtp_port,
            password=self.email_delivery_settings.smtp_password,
            use_tls=self.email_delivery_settings.use_tls,
        )
        await smtp_client.connect()
        await smtp_client.send_message(mime_message)
        await smtp_client.quit()

    async def send_notification(self, *, message: Message) -> bool:
        mime_message = MIMEText(message.message)
        mime_message["From"] = self.email_delivery_settings.smtp_user
        mime_message["To"] = message.user.email
        mime_message["Subject"] = message.subject
        try:
            await self._send_with_send_message(mime_message)
            return True
        except SMTPException as ex:
            logger.exception(ex)
            return False
