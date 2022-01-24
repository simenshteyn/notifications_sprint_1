from functools import lru_cache

from core.settings.template_settings import EndpointTemplateServiceSettings
from services.template.endpoint_template_service import EndpointTemplateService

end_point_template_service: EndpointTemplateService | None = None


def set_end_point_template_service(
    endpoint_template_settings: EndpointTemplateServiceSettings,
) -> EndpointTemplateService:
    return EndpointTemplateService(endpoint_template_settings=endpoint_template_settings)


@lru_cache
def get_end_point_template_service() -> EndpointTemplateService | None:
    return end_point_template_service
