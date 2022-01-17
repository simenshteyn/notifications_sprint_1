from typing import Any
from uuid import UUID

# from core.settings.core_settings import get_settings
from core.settings.user_service_settings import AuthUserSettings
from models.user import User
from services.user.base_user_service import BaseUserService


class AuthUserService(BaseUserService):
    def __init__(self, auth_user_settings: AuthUserSettings, *args, **kwargs):
        pass

    def get_private_user_data(self, user_id: UUID) -> dict[str, Any]:
        pass

    def get_batch_private_users_data(self, users_ids: list[UUID]) -> tuple[User] | None:
        pass


# auth_user_service = AuthUserService(
#     auth_user_settings=get_settings().user_services_settings.auth_user_settings
# )
