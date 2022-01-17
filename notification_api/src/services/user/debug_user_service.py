from datetime import date
from typing import Any
from uuid import UUID

from models.user import User
from services.user.base_user_service import BaseUserService


class DebugUserService(BaseUserService):
    def __init__(self, *args, **kwargs):
        debug_user1 = User(
            user_id=UUID(),
            user_name="test_user1_name",
            user_last_name="test_user1_lastname",
            email="test_user1@test.com",
            phone_number="+79101231234",
            telegram_user_name="telegram1",
            location="Moscow",
            birthdate=date(2005, 7, 14),
        )

        debug_user2 = User(
            user_id=UUID(),
            user_name="test_user2_name",
            user_last_name="test_user2_lastname",
            email="test_user2@test.com",
            phone_number="+79101231235",
            telegram_user_name="telegram2",
            location="Moscow",
            birthdate=date(2005, 7, 13),
        )

        self.debug_user = debug_user1
        self.debug_users = list[debug_user1, debug_user2]

    def get_private_user_data(self, user_id: UUID) -> User:
        return self.debug_user

    def get_batch_private_users_data(self, users_ids: list[UUID]) -> tuple[User]:
        return self.debug_users


debug_user_service = DebugUserService()
