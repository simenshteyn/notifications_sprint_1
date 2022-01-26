import asyncio

import aiohttp
import aioredis
import pytest
from redis import Redis

from tests.functional.settings import config
from tests.functional.utils.models import HTTPResponse

redis_details = {"host": config.redis_host, "port": config.redis_port}


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture(scope="session")
def make_get_request(session):
    async def inner(method: str, params: dict = None, headers: dict = None) -> HTTPResponse:
        params = params or {}
        headers = headers or {}
        url = "{protocol}://{host}:{port}/api/v{api_version}/{method}".format(
            protocol=config.service_protocol,
            host=config.service_host,
            port=config.service_port,
            api_version=config.service_api_version,
            method=method,
        )
        async with session.get(url, params=params, headers=headers) as resp:
            return HTTPResponse(
                body=await resp.json(),
                headers=resp.headers,
                status=resp.status,
            )

    return inner


@pytest.fixture(scope="session")
def make_post_request(session):
    async def inner(method: str, json: dict = None, headers: dict = None) -> HTTPResponse:
        json = json or {}
        headers = headers or {}
        url = "{protocol}://{host}:{port}/api/v{api_version}/{method}".format(
            protocol=config.service_protocol,
            host=config.service_host,
            port=config.service_port,
            api_version=config.service_api_version,
            method=method,
        )
        async with session.post(url, json=json, headers=headers) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner


@pytest.fixture(scope="session")
def make_delete_request(session):
    async def inner(
        method: str, params: dict = None, json: dict = None, headers: dict = None
    ) -> HTTPResponse:
        params = params or {}
        headers = headers or {}
        json = json or {}
        url = "{protocol}://{host}:{port}/api/v{api_version}/{method}".format(
            protocol=config.service_protocol,
            host=config.service_host,
            port=config.service_port,
            api_version=config.service_api_version,
            method=method,
        )
        async with session.delete(url, params=params, json=json, headers=headers) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner


@pytest.fixture(scope="session")
def make_patch_request(session):
    async def inner(
        method: str, params: dict = None, json: dict = None, headers: dict = None
    ) -> HTTPResponse:
        params = params or {}
        headers = headers or {}
        json = json or {}
        url = "{protocol}://{host}:{port}/api/v{api_version}/{method}".format(
            protocol=config.service_protocol,
            host=config.service_host,
            port=config.service_port,
            api_version=config.service_api_version,
            method=method,
        )
        async with session.patch(url, params=params, json=json, headers=headers) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner


@pytest.fixture
def redis_conn():
    r = Redis(redis_details["host"], redis_details["port"])
    yield r
    r.close()


@pytest.fixture(scope="session")
async def redis_client():
    pool = aioredis.ConnectionPool.from_url(
        f"redis://{config.redis_host}:{config.redis_port}",
        encoding="utf-8",
        decode_responses=True,
    )
    redis = aioredis.Redis(connection_pool=pool)
    await redis.flushall()
    yield redis
    await pool.disconnect()
