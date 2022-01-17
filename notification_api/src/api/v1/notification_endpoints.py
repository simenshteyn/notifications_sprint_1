from http import HTTPStatus

from fastapi import APIRouter
from models.event import Event

notifications_router = APIRouter()


@notifications_router.post(
    "/send", summary="Single notification edpoint", status_code=HTTPStatus.ACCEPTED
)
async def send_one(
    event: Event,  # , producer: AIOKafkaProducer = Depends(get_aioproducer)
):
    """Endpoint for single user notification"""

    return {}


@notifications_router.post(
    "/send_batch",
    summary="Batch notifications edpoint",
    status_code=HTTPStatus.ACCEPTED,
)
async def send_batch(
    events: list[Event],
    status_code=HTTPStatus.ACCEPTED,
):
    """Endpoint for batch users notifications"""

    return {}
