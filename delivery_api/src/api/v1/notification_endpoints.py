import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from dependencies.delivery_dependencies import get_delivery_services
from dependencies.message_api_dependecies import get_message_api_service
from models.event import Event
from models.message import Message
from services.delivery import BaseDeliveryService
from services.message.base_message_service import BaseMessageService

logger = logging.getLogger("delivery_api")

notifications_router = APIRouter()


@notifications_router.post("/send", summary="Single notification edpoint", status_code=HTTPStatus.ACCEPTED)
async def send_one(
    event: Event,
    delivery_services: dict[str, BaseDeliveryService] = Depends(get_delivery_services),
    message_api_service: BaseMessageService = Depends(get_message_api_service),
):
    """Endpoint for single user notification"""

    logger.debug(event)

    message: Message | None = await message_api_service.get_message(
        template_id=event.template_id, user_id=event.user_id, event_id=event.event_id
    )
    logger.debug(message)
    if message is None:
        raise HTTPException(status_code=HTTPStatus.EXPECTATION_FAILED, detail={"error": "message is None"})
    result = await delivery_services[event.delivery_type].send_notification(message=message)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED, detail={"error": "couldn't sent notification"}
        )

    return {"result": f"event {event.event_id} has been sended"}
