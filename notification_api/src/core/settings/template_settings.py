from functools import lru_cache

from pydantic import BaseSettings, Field


class EndpointTemplateServiceSettings(BaseSettings):
    endpoint: str = Field("localhost:8001/get_template", env="TEMPLATE_ENDPOINT")


class TemplateServiceSettings(BaseSettings):
    endpoint_settings = EndpointTemplateServiceSettings()


@lru_cache
def get_template_settings(is_debug: bool = False) -> TemplateServiceSettings:
    return TemplateServiceSettings()
