from functools import lru_cache

from pydantic import BaseSettings, Field

from core.settings.delivery_settings import DeliverySettings, get_delivery_settings
from core.settings.message_api_settings import (
    MessageAPISettings,
    get_message_api_settings,
)


class AppSettings(BaseSettings):
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")
    is_debug: bool = Field(False, env="DEBUG")
    should_reload: bool = Field(True, env="SHOULD_RELOAD")
    user_service_name: str = Field("AUTH_USER_SERVICE", env="USER_SERVICE")


class Settings(BaseSettings):
    app = AppSettings()
    delivery_settings: DeliverySettings = get_delivery_settings()
    message_api_settings: MessageAPISettings = get_message_api_settings()


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
