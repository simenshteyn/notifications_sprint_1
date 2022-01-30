from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Body

from models.message import (
    MessageCreate,
    MessageCreateCustom,
    MessageCustom,
    MessageRead,
)
from services.extractor import ExtractorService, get_extractor_service
from services.message import MessageService, get_message_service

router = APIRouter()


@router.post("/user", response_model=MessageRead, response_model_exclude_unset=True)
async def render_message_for_user(
    message: MessageCreate = Body(..., description="UUID of user and UUID of template to generate message"),
    message_service: MessageService = Depends(get_message_service),
    extractor_service: ExtractorService = Depends(get_extractor_service),
) -> MessageRead:
    """Render message for user with given template"""
    result = await message_service.render_message_for_user(
        template_id=message.template_id,
        user_id=message.user_id,
        extractor=extractor_service,
    )
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result


@router.post("/custom", response_model=MessageCustom, response_model_exclude_unset=True)
async def render_custom_message(
    message: MessageCreateCustom = Body(
        ...,
        description="UUID of template and payload JSON with variables to insert into message",
        example='{ "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",'
        '"payload":'
        ' {"first": "first_value", "second": "second value"}}',
    ),
    message_service: MessageService = Depends(get_message_service),
) -> MessageCustom:
    """Render custom message with date provided in payload dictionary."""
    result = await message_service.render_custom_message(
        template_id=message.template_id,
        payload=message.payload,
    )
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result
