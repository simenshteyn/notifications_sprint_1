import uuid as uuid_pkg

from sqlmodel import Field, SQLModel


class TemplatesBase(SQLModel):
    name: str
    content: str


class Templates(TemplatesBase, table=True):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class TemplatesCreate(TemplatesBase):
    pass


class TemplatesUpdate(TemplatesBase):
    id: uuid_pkg.UUID


class TemplatesRead(TemplatesBase):
    id: uuid_pkg.UUID
