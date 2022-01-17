from functools import lru_cache

from core.settings.notification_settings import (
    NotificationSettings,
    get_notification_settings,
)
from core.settings.user_service_settings import UserSettings, get_user_services_settings
from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")
    is_debug: bool = Field(True, env="DEBUG")
    should_reload: bool = Field(True, env="SHOULD_RELOAD")


class Settings(BaseSettings):
    app = AppSettings()
    notification_settings: NotificationSettings = get_notification_settings()
    user_services_settings: UserSettings = get_user_services_settings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
