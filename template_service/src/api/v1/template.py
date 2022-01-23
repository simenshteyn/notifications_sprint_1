from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from models.template import (Templates, TemplatesCreate, TemplatesRead,
                             TemplatesUpdate)
from services.template import TemplateService, get_template_service

router = APIRouter()


@router.get('/{template_id}',
            response_model=TemplatesRead, response_model_exclude_unset=True)
async def get_template_by_id(
        template_id: UUID,
        template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    result = await template_service.get_template_by_id(template_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return result


@router.post('/', response_model=TemplatesRead,
             response_model_exclude_unset=True)
async def add_template(
        template: TemplatesCreate,
        template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    result = await template_service.add_template(
        name=template.name,
        content=template.content,
    )
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result


@router.patch('/', response_model=TemplatesRead,
              response_model_exclude_unset=True)
async def edit_template(
        template: TemplatesUpdate,
        template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    result = await template_service.edit_template(
        template_id=template.id,
        name=template.name,
        content=template.content,
    )
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result


@router.delete('/{template_id}',
               response_model=TemplatesRead, response_model_exclude_unset=True)
async def remove_template_id(
        template_id: UUID,
        template_service: TemplateService = Depends(get_template_service)
) -> Templates:
    result = await template_service.remove_template_by_id(template_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return result
