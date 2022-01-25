import logging
from functools import lru_cache
from string import Template
from uuid import UUID

from fastapi import Depends
from sqlalchemy.engine import Engine
from sqlmodel import Session

from db.orm import get_engine
from models.message import MessageCustom, MessageRead
from models.template import Templates
from models.user import User
from services.extractor import ExtractorService

logger = logging.getLogger(__name__)


class MessageService:
    """Class to render messages from templates by user or custom data."""

    def __init__(self, engine: Engine):
        self.engine = engine

    async def render_message_for_user(
            self,
            template_id: UUID,
            user_id: UUID,
            extractor: ExtractorService,
    ) -> MessageRead | None:
        """Render message for user with template."""
        user: User = await extractor.get_user_data(user_id=user_id)
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            if template is None:
                return None
            text = Template(template.content)
            subject = template.subject
            if subject:
                subject = Template(subject).substitute(user.dict())
            try:
                msg = text.substitute(user.dict())
                return MessageRead(template_id=template_id,
                                   user=user,
                                   subject=subject,
                                   message=msg)
            except Exception as e:
                logger.debug(f'{e}')
                return None

    async def render_custom_message(
            self, template_id: UUID, payload: dict) -> MessageCustom | None:
        """Render custom message with provided data in payload."""
        with Session(self.engine) as session:
            template = session.get(Templates, template_id)
            if template is None:
                return None
            text = Template(template.content)
            try:
                msg = text.substitute(payload)
                return MessageCustom(template_id=template_id,
                                     payload=payload,
                                     message=msg)
            except Exception as e:
                logger.debug(f'{e}')
                return None


@lru_cache()
def get_message_service(
        engine: Engine = Depends(get_engine)) -> MessageService:
    return MessageService(engine)
