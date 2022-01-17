from functools import lru_cache

from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")
    is_debug: bool = Field(True, env="DEBUG")
    should_reload: bool = Field(True, env="SHOULD_RELOAD")


#     should_check_jwt: bool = Field(False, env="SHOULD_CHECK_JWT")
#     jwt_public_key = Field("JWT_PUBLIC_KEY", env="JWT_PUBLIC_KEY")
#     jwt_algorithm = Field("HS256", env="JWT_ALGORITHM")


# class KafkaSettings(BaseSettings):
#     hosts: list[str] = Field(["127.0.0.1:29092"], env="KAFKA_HOSTS")
#     topics: list[str] = Field(
#         [
#             "movie_like",
#             "movie_dislike",
#             "movie_share",
#             "movie_comment",
#             "movie_watch_history",
#         ],
#         env="KAFKA_TOPIC",
#     )
#     project_name: str = Field("movie_kafka_producer", env="PROJECT_NAME")


# class RedisSettings(BaseSettings):
#     endpoint: str = Field("127.0.0.1", env="REDIS_HOST")
#     port: int = Field(6379, env="REDIS_PORT")


# class SentrySettings(BaseSettings):
#     sdk: str = Field("", env="SENTRY_DSN")
#     traces_sample_rate: float = 1.0


# class LogstashSettings(BaseSettings):
#     host: str = Field("localhost", env="LOGSTASH_HOST")
#     port: int = Field(5044, env="LOGSTASH_PORT")


class Settings(BaseSettings):
    app = AppSettings()
    # kafka_settings = KafkaSettings()
    # redis_settings = RedisSettings()
    # sentry_settings = SentrySettings()
    # logstash_settings = LogstashSettings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
