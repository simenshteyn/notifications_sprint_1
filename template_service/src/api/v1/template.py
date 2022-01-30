from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from schema.template import (
    Templates,
    TemplatesCreate,
    TemplatesRead,
    TemplatesShort,
    TemplatesUpdate,
)
from services.template import TemplateService, get_template_service

router = APIRouter()


@router.get("/", response_model=list[TemplatesShort], response_model_exclude_unset=True)
async def get_templates(
    limit: int = 50, offset: int = 0, template_service: TemplateService = Depends(get_template_service)
) -> list[Templates]:
    """Get list of templates with limit and offset."""
    result = await template_service.get_template_list(limit=limit, offset=offset)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return result


@router.get("/{template_id}", response_model=TemplatesRead, response_model_exclude_unset=True)
async def get_template_by_id(
    template_id: UUID, template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    """Get template by UUID."""
    result = await template_service.get_template_by_id(template_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return result


@router.post("/", response_model=TemplatesRead, response_model_exclude_unset=True)
async def add_template(
    template: TemplatesCreate, template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    """Add new template with name, content and subject."""
    result = await template_service.add_template(
        name=template.name,
        content=template.content,
        subject=template.subject,
    )
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result


@router.patch("/", response_model=TemplatesRead, response_model_exclude_unset=True)
async def edit_template(
    template: TemplatesUpdate, template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    """Edit template with new name, content of subject by UUID."""
    result = await template_service.edit_template(
        template_id=template.id,
        name=template.name,
        content=template.content,
        subject=template.subject,
    )
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result


@router.delete("/{template_id}", response_model=TemplatesRead, response_model_exclude_unset=True)
async def remove_template_id(
    template_id: UUID, template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    """Remove template by UUID."""
    result = await template_service.remove_template_by_id(template_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return result
