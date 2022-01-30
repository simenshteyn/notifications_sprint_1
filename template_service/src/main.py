import logging

import aioredis
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import message, template
from core import config
from core.logger import LOGGING_CONFIG
from db import redis
from db.orm import create_db_and_tables

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=config.PROJECT_NAME,
    version="1.0.0",
    description="Asynchronous API to handle notification templates",
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json",
    redoc_url="/api/v1/redoc",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    redis.redis = aioredis.from_url(
        f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}",
        encoding="utf-8",
        decode_response=True,
    )
    await create_db_and_tables()


@app.on_event("shutdown")
async def shutdown():
    await redis.redis.close()


app.include_router(
    template.router,
    prefix="/api/v1/template",
    tags=["template"],
)
app.include_router(
    message.router,
    prefix="/api/v1/message",
    tags=["message"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8888,
        log_config=LOGGING_CONFIG,
        log_level=logging.DEBUG,
    )
