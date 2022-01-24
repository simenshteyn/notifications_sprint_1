from uuid import UUID

import orjson
from pydantic import BaseModel

from models.user import User


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class Orjson(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class MessageRead(Orjson):
    template_id: UUID
    user: User
    subject: str | None
    message: str


class MessageCreate(Orjson):
    template_id: UUID
    user_id: UUID


class MessageCreateCustom(Orjson):
    template_id: UUID
    payload: dict


class MessageCustom(Orjson):
    template_id: UUID
    payload: dict
    message: str
