from functools import lru_cache
from string import Template
from uuid import UUID

from fastapi import Depends
from sqlalchemy.engine import Engine
from sqlmodel import Session

from db.orm import get_engine
from models.message import MessageCustom, MessageRead
from models.template import Templates
from services.extractor import ExtractorService


class MessageService:
    """Class to render messages from templates by user or custom data."""

    def __init__(self, engine: Engine):
        self.engine = engine

    async def render_message_for_user(
            self,
            template_id: UUID,
            user_id: UUID,
            extractor: ExtractorService,
    ) -> MessageRead:
        """Render message for user with template."""
        user = await extractor.get_user_data(user_id=user_id)
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            if template:
                text = Template(template.content)
                try:
                    msg = text.substitute(user.dict())
                    return MessageRead(template_id=template_id,
                                       user_id=user_id,
                                       message=msg)
                except Exception as e:
                    return None
            return template

    async def render_custom_message(
            self, template_id: UUID, payload: dict) -> MessageCustom:
        """Render custom message with provided data in payload."""
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            if template:
                text = Template(template.content)
                try:
                    msg = text.substitute(payload)
                    return MessageCustom(template_id=template_id,
                                         payload=payload,
                                         message=msg)
                except Exception as e:
                    return None
            return template

    def validate_message(self, message: str) -> bool:
        return True if message else False


@lru_cache()
def get_message_service(
        engine: Engine = Depends(get_engine)) -> MessageService:
    return MessageService(engine)
