from functools import lru_cache

from pydantic import BaseSettings, Field

from core.settings.delivery_settings import DeliverySettings, get_delivery_settings
from core.settings.template_settings import (
    TemplateServiceSettings,
    get_template_settings,
)
from core.settings.user_service_settings import UserSettings, get_user_services_settings
from services.user import AuthUserService, BaseUserService, DebugUserService


class AppSettings(BaseSettings):

    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")
    is_debug: bool = Field(True, env="DEBUG")
    should_reload: bool = Field(True, env="SHOULD_RELOAD")
    # user_service_name: str = Field("AUTH_USER_SERVICE", env="USER_SERVICE")
    # TODO remove after debug
    user_service_name: str = Field("DEBUG_USER_SERVICE", env="USER_SERVICE")

    user_service: BaseUserService | None


class Settings(BaseSettings):
    app = AppSettings()
    delivery_settings: DeliverySettings = get_delivery_settings()
    user_services_settings: UserSettings = get_user_services_settings()
    template_services_settings: TemplateServiceSettings = get_template_settings()


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
