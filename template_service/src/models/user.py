from datetime import date
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    user_id: UUID
    user_name: str
    user_last_name: str
    email: str | None
    phone_number: str | None
    telegram_user_name: str | None
    location: str | None
    birthdate: date | None
