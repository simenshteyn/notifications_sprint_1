from functools import lru_cache

from pydantic import BaseSettings, Field


class DeliveryAPISettings(BaseSettings):
    host: str = Field("0.0.0.0", env="API_HOST")
    port: int = Field(8000, env="API_PORT")


class RabbitSettings(BaseSettings):
    server_url: str = Field("amqp://guest:guest@localhost:5672", env="AMQP_SERVER_URL")
    queue_name: str = Field("notification_queue", env="RABBIT_QUEUE_NAME")


class AppSettings(BaseSettings):
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")


class Settings(BaseSettings):
    app = AppSettings()
    rabbit_settings = RabbitSettings()
    delivery_settings = DeliveryAPISettings()


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
