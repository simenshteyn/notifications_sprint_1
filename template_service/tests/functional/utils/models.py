from dataclasses import dataclass
from uuid import UUID

from multidict import CIMultiDictProxy
from pydantic import BaseModel


@dataclass
class HTTPResponse:
    body: dict
    headers: CIMultiDictProxy[str]
    status: int


class StatusMessage(BaseModel):
    detail: str


class TemplatesBase(BaseModel):
    name: str


class Templates(TemplatesBase):
    subject: str | None = None
    content: str
    id: UUID


class TemplatesCreate(TemplatesBase):
    subject: str | None
    content: str
    pass


class TemplatesUpdate(TemplatesBase):
    subject: str | None
    content: str
    id: UUID


class TemplatesRead(TemplatesBase):
    subject: str | None
    content: str
    id: UUID


class TemplatesShort(TemplatesBase):
    id: UUID
