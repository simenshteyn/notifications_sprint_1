from redis import Redis

from tests.functional.settings import config


def test_redis_server_connection():
    r = Redis(host=config.redis_host, port=config.redis_port)
    is_connected = r.ping()
    assert is_connected
