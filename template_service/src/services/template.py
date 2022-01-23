from functools import lru_cache
from uuid import UUID

from fastapi import Depends
from sqlalchemy.engine import Engine
from sqlmodel import Session

from db.orm import get_engine
from models.template import Templates


class TemplateService:
    """Class to interact with templates: create, edit, read raw, delete."""

    def __init__(self, engine: Engine):
        self.engine = engine

    async def get_template_by_id(self, template_id: UUID) -> Templates:
        """Get template by ID"""
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            return template

    async def add_template(self, name: str, content: str) -> Templates:
        """Add new template to storage with template name and content."""
        template = Templates(name=name, content=content)
        with Session(self.engine) as session:
            session.add(template)
            session.commit()
            session.refresh(template)
        return template

    async def edit_template(
            self, template_id: UUID, name: str, content: str) -> Templates:
        """Update template by id with new name or content"""
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            if template:
                template.name = name
                template.content = content
                session.add(template)
                session.commit()
                session.refresh(template)
            return template

    async def remove_template_by_id(self, template_id: UUID) -> Templates:
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
