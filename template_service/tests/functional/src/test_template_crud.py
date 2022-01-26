from http import HTTPStatus

import pytest

from tests.functional.utils.extract import (
    extract_message,
    extract_template,
    extract_templates,
)


@pytest.mark.asyncio
async def test_template_endpoint_crud(
    make_get_request, make_post_request, make_delete_request, make_patch_request
):
    """Test template CRUD cycle: add, edit, read, delete template."""
    # Add new template
    response = await make_post_request(
        "template/", json={"name": "test_template_42", "subject": "test subject", "content": "test content"}
    )
    template = await extract_template(response)
    template_uuid = str(template.id)
    assert template.name == "test_template_42"
    assert template.subject == "test subject"
    assert template.content == "test content"
    assert len(template_uuid)

    # Read new template
    response = await make_get_request(f"template/{template_uuid}")
    template = await extract_template(response)
    assert response.status == HTTPStatus.OK
    assert template.name == "test_template_42"
    assert template.subject == "test subject"
    assert template.content == "test content"
    assert str(template.id) == template_uuid

    # Read template list
    response = await make_get_request("template/")
    templates = await extract_templates(response)
    assert response.status == HTTPStatus.OK
    assert len(templates) > 0

    # Edit new template
    response = await make_patch_request(
        "template/",
        json={
            "name": "test_template_43",
            "subject": "test subject edited",
            "content": "test content edited",
            "id": template_uuid,
        },
    )
    template = await extract_template(response)
    assert response.status == HTTPStatus.OK
    assert template.name == "test_template_43"
    assert template.subject == "test subject edited"
    assert template.content == "test content edited"
    assert str(template.id) == template_uuid

    # Delete new template
    response = await make_delete_request(f"template/{template_uuid}")
    template = await extract_template(response)
    assert response.status == HTTPStatus.OK
    assert template.name == "test_template_43"
    assert template.subject == "test subject edited"
    assert template.content == "test content edited"
    assert str(template.id) == template_uuid

    # Check deleted template can't be found
    response = await make_get_request(f"template/{template_uuid}")
    message = await extract_message(response)
    assert response.status == HTTPStatus.NOT_FOUND
    assert message.detail == "Not Found"
