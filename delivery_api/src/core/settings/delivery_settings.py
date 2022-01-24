from functools import lru_cache

from pydantic import BaseSettings, Field


class EmailDeliverySettings(BaseSettings):
    smtp_server: str = Field("smtp.yandex.ru", env="SMTP_SERVER")
    smtp_port: int = Field(465, env="SMTP_PORT")
    smtp_user: str = Field("prakticum@yandex.ru", env="SMTP_USER")
    smtp_password: str = Field("prakticum_pswd", env="SMTP_PASSWORD")
    use_tls: bool = Field(True, env="USE_TLS")


class DeliverySettings(BaseSettings):
    email_settings = EmailDeliverySettings()


@lru_cache
def get_delivery_settings(is_debug: bool = False) -> DeliverySettings:
    return DeliverySettings()
