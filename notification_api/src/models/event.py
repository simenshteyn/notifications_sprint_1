from uuid import UUID

from pydantic import BaseModel


class Event(BaseModel):
    user_id: UUID
    delivery_type: str
    event_type: str | None
    template_id: str | None
    specific_func: str | None
