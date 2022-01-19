import asyncio
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.notification_endpoints import notifications_router
from core.logger import LOGGING
from core.settings.core_settings import get_settings
from dependencies import (
    delivery_dependencies,
    template_dependencies,
    user_storage_dependencies,
)
from services.delivery import EmailDeliveryService
from services.template.endpoint_template_service import EndpointTemplateService

app_settings = get_settings()

event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

logger = logging.getLogger("notification_api")
logger.setLevel(logging.INFO if not app_settings.app.is_debug else logging.DEBUG)
logger.setLevel(logging.DEBUG)


app = FastAPI(
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    title="Post-only Notification API для онлайн-кинотеатра",
    description="Служба нотификации",
    version="0.1.0",
)


@app.on_event("startup")
async def startup_event():
    # подключение службы получения персональных данных согласно конфига
    user_storage_dependencies.user_service = user_storage_dependencies.set_user_service(
        service_name=app_settings.app.user_service_name,
        services_settings=app_settings.user_services_settings,
    )
    logger.debug(user_storage_dependencies.get_user_service())

    # подключение служб отправки уведомлений согласно конфига
    delivery_dependencies.delivery_services["email"] = EmailDeliveryService(
        email_notification_settings=app_settings.delivery_settings.email_settings, event_loop=event_loop
    )

    # подгрузка службы для тестирования
    if app_settings.app.is_debug:
        from services.delivery import DebugDeliveryService

        delivery_dependencies.delivery_services["debug"] = DebugDeliveryService()
    logger.debug(delivery_dependencies.delivery_services)

    # подгрузка службы работы с шаблонами
    template_dependencies.end_point_template_service = EndpointTemplateService(
        endpoint_template_settings=app_settings.template_services_settings.endpoint_settings
    )

    logger.debug(template_dependencies.end_point_template_service)


app.include_router(notifications_router, prefix="/api/v1", tags=["Notifications service"])

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=app_settings.app.host,
        port=app_settings.app.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=app_settings.app.should_reload,
    )
