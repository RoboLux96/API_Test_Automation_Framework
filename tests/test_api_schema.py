import pytest
from jsonschema import validate, ValidationError

from schemas.post_schema import POST_SCHEMA


def test_post_response_matches_schema(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200

    response_data = response.json()

    validate(
        instance=response_data,
        schema=POST_SCHEMA,
    )


def test_post_schema_rejects_invalid_data():
    invalid_post = {
    "userId": "one",
    "id": 1,
    "title": "Test title",
    "body": "Test body",
    }
   
    with pytest.raises(ValidationError):
        validate(
            instance=invalid_post,
            schema=POST_SCHEMA,
        ) 
