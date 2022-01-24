from tests.functional.utils.models import HTTPResponse, StatusMessage, \
    TemplatesRead, TemplatesShort


async def extract_message(response: HTTPResponse) -> StatusMessage:
    status = response.body
    return StatusMessage.parse_obj(status)


async def extract_template(response: HTTPResponse) -> TemplatesRead:
    template = response.body
    return TemplatesRead.parse_obj(template)


async def extract_templates(response: HTTPResponse) -> list[TemplatesShort]:
    templates = response.body
    return [TemplatesShort.parse_obj(template) for template in templates]
