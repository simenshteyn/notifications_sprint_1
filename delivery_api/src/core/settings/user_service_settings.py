from functools import lru_cache

from pydantic import BaseSettings, Field


class AuthUserSettings(BaseSettings):
    host: str = Field("0.0.0.0", env="AUTH_HOST")
    port: int = Field(8000, env="AUTH_PORT")


class BDUserSettings(BaseSettings):
    sqlalchemy_database_url: str = Field(
        "postgresql+psycopg2://postgres:1234@localhost:5432/online_movie_theater_db",
        env="SQLALCHEMY_DATABASE_URI",
    )


class UserSettings(BaseSettings):
    auth_user_settings = AuthUserSettings()
    bd_user_settings = BDUserSettings()


@lru_cache
def get_user_services_settings(is_debug: bool = False) -> UserSettings:
    return UserSettings()
