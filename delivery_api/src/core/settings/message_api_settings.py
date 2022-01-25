from functools import lru_cache

from pydantic import BaseSettings, Field


class MessageAPISettings(BaseSettings):
    host: str = Field("http://localhost:8001", env="MESSAGE_HOST")
    endpoint: str = Field("/api/v1/message/user", env="MESSAGE_ENDPOINT")


@lru_cache
def get_message_api_settings(is_debug: bool = False) -> MessageAPISettings:
    return MessageAPISettings()
