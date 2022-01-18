from core.settings.core_settings import get_settings
from core.settings.user_service_settings import UserSettings
from services.user import AuthUserService, BaseUserService, DBUserService

user_service: BaseUserService | None = None


def set_user_service(service_name: str, services_settings: UserSettings) -> BaseUserService:

    match service_name:
        case "AUTH_USER_SERVICE":
            return AuthUserService(services_settings.auth_user_settings)
        case "DB_USER_SERVICE":
            return AuthUserService(services_settings.bd_user_settings)
        case "DEBUG_USER_SERVICE":

            if get_settings().app.is_debug:
                from services.user import DebugUserService

                return DebugUserService()


def get_user_service() -> BaseUserService | None:
    return user_service
