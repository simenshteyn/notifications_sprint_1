import logging
from http import HTTPStatus

from dependencies.user_storage_dependencies import get_user_service
from fastapi import APIRouter, Depends
from models.event import Event
from models.user import User
from services.user import BaseUserService

logger = logging.getLogger("notification_api")

notifications_router = APIRouter()


@notifications_router.post(
    "/send", summary="Single notification edpoint", status_code=HTTPStatus.ACCEPTED
)
async def send_one(
    event: Event, user_service: BaseUserService = Depends(get_user_service)
):
    """Endpoint for single user notification"""
    user: User = user_service.get_private_user_data(user_id=event.user_id)
    logger.debug(user)
    return {}


@notifications_router.post(
    "/send_batch",
    summary="Batch notifications edpoint",
    status_code=HTTPStatus.ACCEPTED,
)
async def send_batch(
    events: list[Event],
    status_code=HTTPStatus.ACCEPTED,
    user_service: BaseUserService = Depends(get_user_service),
):
    """Endpoint for batch users notifications"""
    users: list[User] = user_service.get_batch_private_users_data(
        users_ids=(event.user_id for event in events)
    )
    logger.debug(users)
    return {}
