from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from core.settings.user_service_settings import AuthUserSettings
from models.user import User
from services.user.base_user_service import BaseUserService


class AuthUserService(BaseUserService):
    def __init__(self, *, auth_user_settings: AuthUserSettings):
        self.endpoint: str = f"{auth_user_settings.host}:{auth_user_settings.port}"

    async def get_private_user_data(self, *, user_id: UUID) -> User | None:
        async with httpx.AsyncClient() as client:
            response = await client.post(self.endpoint, params={"user_id": str(user_id)})
        if response.status_code not in (HTTPStatus.ACCEPTED, HTTPStatus.OK):
            return None
        return User(**response.json())
