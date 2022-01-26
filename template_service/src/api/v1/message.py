from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

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
    message: MessageCreate,
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
    message: MessageCreateCustom, message_service: MessageService = Depends(get_message_service)
) -> MessageCustom:
    """Render custom message with date provided in payload dictionary."""
    result = await message_service.render_custom_message(
        template_id=message.template_id,
        payload=message.payload,
    )
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result
