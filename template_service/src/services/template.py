from functools import lru_cache
from uuid import UUID

from fastapi import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from db.orm import get_session
from models.template import Templates


class TemplateService:
    """Class to interact with templates: create, edit, read raw, delete."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_template_list(self, limit: int, offset: int) -> list[Templates] | None:
        """Get template list with limit and offset."""
        statement = select(Templates).offset(offset).limit(limit)
        results = await self.session.exec(statement)
        templates = results.all()
        return templates

    async def get_template_by_id(self, template_id: UUID) -> Templates | None:
        """Get template by ID"""
        template = await self.session.get(Templates, template_id)
        return template

    async def add_template(self, name: str, content: str, subject: str) -> Templates | None:
        """Add new template to storage with template name, content, subject."""
        template = Templates(name=name, content=content, subject=subject)
        self.session.add(template)
        await self.session.commit()
        await self.session.refresh(template)
        return template

    async def edit_template(
        self, template_id: UUID, name: str, content: str, subject: str
    ) -> Templates | None:
        """Update template by id with new name, content or subject."""
        template = await self.session.get(Templates, template_id)
        if template:
            template.name = name
            template.content = content
            template.subject = subject
            self.session.add(template)
            await self.session.commit()
            await self.session.refresh(template)
        return template

    async def remove_template_by_id(self, template_id: UUID) -> Templates | None:
        """Remove template by ID"""
        template = await self.session.get(Templates, template_id)
        if template:
            await self.session.delete(template)
            await self.session.commit()
        return template


@lru_cache()
def get_template_service(session: AsyncSession = Depends(get_session)) -> TemplateService:
    return TemplateService(session)
