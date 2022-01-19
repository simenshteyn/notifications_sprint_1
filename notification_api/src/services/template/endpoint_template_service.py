from http import HTTPStatus
from uuid import UUID

import httpx
from jinja2 import Template

from core.settings.template_settings import EndpointTemplateServiceSettings
from models.user import User
from services.template.base_template_service import BaseTemplateService


class EndpointTemplateService(BaseTemplateService):
    def __init__(self, *, endpoint_template_settings: EndpointTemplateServiceSettings):
        self.endpoint: str = endpoint_template_settings.endpoint
        self.message_body = None

    async def _get_template(self, *, template_id: UUID) -> str | None:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.endpoint, params={"template_id": str(template_id)})
        if response.status_code not in (HTTPStatus.ACCEPTED, HTTPStatus.OK):
            return None
        return str(response.content)

    async def get_message_body(self, *, template_id: UUID, user: User) -> str | None:
        template_body: str | None = await self._get_template(template_id=template_id)
        if template_body is None:
            return None
        template = Template(template_body)
        return template.render(**User.dict(include={"user_name", "user_last_name", "birthdate"}))
