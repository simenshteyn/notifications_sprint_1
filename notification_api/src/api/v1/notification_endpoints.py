import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends

from dependencies.notifications_dependencies import get_email_notification_services
from dependencies.template_dependencies import get_end_point_template_service
from dependencies.user_storage_dependencies import get_user_service
from models.event import Event
from models.user import User
from services.notification import BaseNotificationService
from services.template.endpoint_template_service import EndpointTemplateService
from services.user import BaseUserService

logger = logging.getLogger("notification_api")

notifications_router = APIRouter()


@notifications_router.post("/send", summary="Single notification edpoint", status_code=HTTPStatus.ACCEPTED)
async def send_one(
    event: Event,
    user_service: BaseUserService = Depends(get_user_service),
    notification_services: dict[str, BaseNotificationService] = Depends(get_email_notification_services),
    end_point_template_service: EndpointTemplateService = Depends(get_end_point_template_service),
):
    """Endpoint for single user notification"""

    logger.debug(event)

    user: User = user_service.get_private_user_data(user_id=event.user_id)
    logger.debug(user)
    logger.debug(notification_services[event.delivery_type])
    return {}


@notifications_router.post(
    "/send_batch",
    summary="Batch notifications edpoint",
    status_code=HTTPStatus.ACCEPTED,
)
async def send_batch(
    events: list[Event],
    user_service: BaseUserService = Depends(get_user_service),
    notification_services: dict[str, BaseNotificationService] = Depends(get_email_notification_services),
    end_point_template_service: EndpointTemplateService = Depends(get_end_point_template_service),
):
    """Endpoint for batch users notifications"""
    users: list[User] = user_service.get_batch_private_users_data(
        users_ids=(event.user_id for event in events)
    )
    logger.debug(users)
    return {}
