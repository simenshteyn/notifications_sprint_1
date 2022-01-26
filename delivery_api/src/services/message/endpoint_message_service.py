import logging
from functools import lru_cache
from http import HTTPStatus
from uuid import UUID

import aiohttp

from core.settings.message_api_settings import MessageAPISettings
from models.event import Event
from models.message import Message
from models.user import User
from services.message.base_message_service import BaseMessageService

logger = logging.getLogger("delivery_api")


class EndpointMessageAPIService(BaseMessageService):
    def __init__(self, *args, **kwargs) -> None:
        settings: MessageAPISettings = kwargs["settings"]
        self.endpoint = f"{settings.host}{settings.endpoint}"

    async def get_message(self, *, user_id: UUID, template_id: UUID, event_id: UUID) -> Message | None:

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.endpoint, params={"template_id": str(template_id), "user_id": str(user_id)}
                ) as resp:
                    response_json = await resp.json()
        except aiohttp.client_exceptions.ClientError as ex:
            logger.exception(ex)
            return None

        user = User(**response_json["user"])
        return Message(
            user=user,
            event_id=event_id,
            subject=response_json["subject"],
            message=response_json["message"],
        )
