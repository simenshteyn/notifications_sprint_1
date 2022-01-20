import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from dependencies.delivery_dependencies import get_delivery_services
from dependencies.notification_dependecies import get_notification_service
from dependencies.user_storage_dependencies import get_user_service
from models.event import Event
from models.notification import Notification
from models.user import User
from services.delivery import BaseDeliveryService
from services.notification.base_notification_service import BaseNotificationService
from services.user import BaseUserService

logger = logging.getLogger("notification_api")

notifications_router = APIRouter()


@notifications_router.post("/send", summary="Single notification edpoint", status_code=HTTPStatus.ACCEPTED)
async def send_one(
    event: Event,
    user_service: BaseUserService = Depends(get_user_service),
    delivery_services: dict[str, BaseDeliveryService] = Depends(get_delivery_services),
    notification_service: BaseNotificationService = Depends(get_notification_service),
):
    """Endpoint for single user notification"""

    logger.debug(event)

    user: User = user_service.get_private_user_data(user_id=event.user_id)
    logger.debug(user)
    if user is None:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail={"error": "couldn't find user"})
    notification: Notification | None = await notification_service.get_notification(event=event, user=user)
    logger.debug(notification)
    if notification is None:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED, detail={"error": "couldn't create notification"}
        )

    result = await delivery_services[event.delivery_type].send_notification(notification=notification)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED, detail={"error": "couldn't sent notification"}
        )

    return {"result": f"event {event.event_id} has been sended"}
