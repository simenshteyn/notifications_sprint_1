from abc import ABC, abstractmethod
from uuid import UUID


class BaseTemplateService(ABC):
    @abstractmethod
    def _get_template(self, *, template_id: UUID) -> str | None:
        raise NotImplemented

    @abstractmethod
    def get_message_body(self, *, template_id: UUID) -> str | None:
        raise NotImplemented
