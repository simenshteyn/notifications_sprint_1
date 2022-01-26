from models.message import Message
from services.delivery.base_delivery_service import BaseDeliveryService


class DebugDeliveryService(BaseDeliveryService):
    def __init__(self, *args, **kwargs):
        pass

    async def send_notification(self, *, message: Message) -> bool:
        print("Sending.......")
        print(message)
        print("Notification has been sent")
        return True
