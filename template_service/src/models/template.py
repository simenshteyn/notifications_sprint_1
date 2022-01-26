import uuid as uuid_pkg

from sqlmodel import Field, SQLModel


class TemplatesBase(SQLModel):
    name: str


class Templates(TemplatesBase, table=True):
    subject: str | None = None
    content: str
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class TemplatesCreate(TemplatesBase):
    subject: str | None
    content: str
    pass


class TemplatesUpdate(TemplatesBase):
    subject: str | None
    content: str
    id: uuid_pkg.UUID


class TemplatesRead(TemplatesBase):
    subject: str | None
    content: str
    id: uuid_pkg.UUID


class TemplatesShort(TemplatesBase):
    id: uuid_pkg.UUID
