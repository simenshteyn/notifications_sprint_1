from functools import lru_cache

from pydantic import BaseSettings, Field


class EmailNotificationSettings(BaseSettings):
    smtp_server: str = Field("smtp.yandex.ru", env="SMTP_SERVER")
    smtp_port: int = Field(465, env="SMTP_PORT")
    smtp_user: str = Field("prakticum@yandex.ru", env="SMTP_USER")
    smtp_password: str = Field("prakticum_pswd", env="SMTP_PASSWORD")


class SMSNotificationSettings(BaseSettings):
    sms_gate: str = Field("0.0.0.0", env="SMS_GATE")
    sms_login: str = Field("sms_login", env="SMS_LOGIN")
    sms_password: str = Field("sms_password", env="SMS_PASSWORD")


class TelegramNotificationSettings(BaseSettings):
    token: str = Field("ABC-DEF1234ghIkl-zyx57W2v1u123ew11", env="TELEGRAM_TOKEN")


class NotificationSettings(BaseSettings):
    email_settings = EmailNotificationSettings()
    sms_settings = SMSNotificationSettings()
    telegram_settings = TelegramNotificationSettings()


@lru_cache
def get_notification_settings(is_debug: bool = False) -> NotificationSettings:
    return NotificationSettings()
