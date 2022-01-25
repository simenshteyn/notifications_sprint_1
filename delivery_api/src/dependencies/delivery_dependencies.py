from core.settings.core_settings import get_settings
from services.delivery import (
    BaseDeliveryService,
    DebugDeliveryService,
    EmailDeliveryService,
)

delivery_services: dict[BaseDeliveryService, str] = {}


def get_delivery_services() -> dict[BaseDeliveryService, str] | None:
    return delivery_services
