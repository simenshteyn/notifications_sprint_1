from uuid import UUID

from pydantic import BaseModel

from models.user import User


class Message(BaseModel):
    event_id: UUID
    user: User
    subject: str | None
    message: str | None
