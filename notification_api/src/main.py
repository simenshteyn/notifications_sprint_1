import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.notification_endpoints import notifications_router
from core.logger import LOGGING
from core.settings.core_settings import get_settings
from dependencies import user_storage_dependencies

app_settings = get_settings()

logger = logging.getLogger("notification_api")
logger.setLevel(logging.INFO if not app_settings.app.is_debug else logging.DEBUG)

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
    user_storage_dependencies.user_service = app_settings.app.user_service

    logger.debug(user_storage_dependencies.get_user_service())


app.include_router(
    notifications_router, prefix="/api/v1", tags=["Notifications service"]
)

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=app_settings.app.host,
        port=app_settings.app.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=app_settings.app.should_reload,
    )
