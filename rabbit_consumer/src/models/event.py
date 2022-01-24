from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class DeliveryType(str, Enum):
    "Delivery types variants"
    email = "email"


class Event(BaseModel):
    "Event for sending notification"
    event_id: UUID
    user_id: UUID
    delivery_type: DeliveryType
    template_id: str or None
