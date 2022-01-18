from functools import lru_cache

from pydantic import BaseSettings, Field

from core.settings.notification_settings import (
    NotificationSettings,
    get_notification_settings,
)
from core.settings.template_settings import (
    TemplateServiceSettings,
    get_template_settings,
)
from core.settings.user_service_settings import UserSettings, get_user_services_settings
from services.user import (
    AuthUserService,
    BaseUserService,
    DBUserService,
    DebugUserService,
)

USER_SERVICES = {"AUTH_USER_SERVICE": AuthUserService, "DB_USER_SERVICE": DBUserService}


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
    notification_settings: NotificationSettings = get_notification_settings()
    user_services_settings: UserSettings = get_user_services_settings()
    template_services_settings: TemplateServiceSettings = get_template_settings()


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
