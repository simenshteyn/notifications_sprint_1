import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.notification_endpoints import notifications_router
from core.logger import LOGGING
from core.settings.core_settings import get_settings

app = FastAPI(
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    title="Post-only Notification API для онлайн-кинотеатра",
    description="Служба нотификации",
    version="0.1.0",
)

app.include_router(
    notifications_router, prefix="/api/v1", tags=["Notifications service"]
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=get_settings().app.host,
        port=get_settings().app.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=get_settings().app.should_reload,
    )
