from enum import Enum
from uuid import UUID

from core.settings.core_settings import get_settings
from pydantic import BaseModel


class DeliveryType(str, Enum):
    "Delivery types variants"
    sms = "sms"
    email = "email"
    if get_settings().app.is_debug:
        debug = "debug"


class Event(BaseModel):
    "Event for sending notification"
    user_id: UUID
    delivery_type: DeliveryType
    event_type: str | None
    template_id: str | None
    specific_func: str | None
