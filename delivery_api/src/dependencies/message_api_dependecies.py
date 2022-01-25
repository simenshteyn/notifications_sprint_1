from functools import lru_cache

from services.message.base_message_service import BaseMessageService

message_api_service: BaseMessageService | None = None


def set_message_api_service(message_service: BaseMessageService, *args, **kwargs) -> BaseMessageService:
    return message_service(*args, **kwargs)


@lru_cache
def get_message_api_service() -> BaseMessageService | None:
    return message_api_service
