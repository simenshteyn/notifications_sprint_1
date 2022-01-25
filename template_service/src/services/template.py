from functools import lru_cache
from uuid import UUID

from fastapi import Depends
from sqlalchemy.engine import Engine
from sqlmodel import Session, select

from db.orm import get_engine
from models.template import Templates


class TemplateService:
    """Class to interact with templates: create, edit, read raw, delete."""

    def __init__(self, engine: Engine):
        self.engine = engine

    async def get_template_list(
            self, limit: int, offset: int) -> list[Templates] | None:
        """Get template list with limit and offset."""
        with Session(self.engine) as session:
            statement = select(Templates).offset(offset).limit(limit)
            results = session.exec(statement)
            templates = results.all()
            return templates

    async def get_template_by_id(self, template_id: UUID) -> Templates | None:
        """Get template by ID"""
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            return template

    async def add_template(
            self, name: str, content: str, subject: str) -> Templates | None:
        """Add new template to storage with template name, content, subject."""
        template = Templates(name=name, content=content, subject=subject)
        with Session(self.engine) as session:
            session.add(template)
            session.commit()
            session.refresh(template)
        return template

    async def edit_template(
            self, template_id: UUID, name: str, content: str, subject: str
    ) -> Templates | None:
        """Update template by id with new name, content or subject."""
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            if template:
                template.name = name
                template.content = content
                template.subject = subject
                session.add(template)
                session.commit()
                session.refresh(template)
            return template

    async def remove_template_by_id(self,
                                    template_id: UUID) -> Templates | None:
        """Remove template by ID"""
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            if template:
                session.delete(template)
                session.commit()
            return template


@lru_cache()
def get_template_service(
        engine: Engine = Depends(get_engine)) -> TemplateService:
    return TemplateService(engine)
