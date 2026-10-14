import pytest
import requests


def test_create_post_returns_201(api_client):
    payload = {
        "title": "Automation testing",
        "body": "Created by an automated API test",
        "userId": 1,
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_update_post_returns_200(api_client):
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1,
    }

    response = api_client.put("/posts/1", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_delete_post_returns_200(api_client):
    response = api_client.delete("/posts/1")

    assert response.status_code == 200


@pytest.mark.parametrize(
    "payload",
    [
        {
            "title": "Missing body",
            "userId": 1,
        },
        {
            "body": "Missing title",
            "userId": 1,
        },
    ],
)
def test_create_post_with_incomplete_payload(api_client, payload):
    response = api_client.post("/posts", json=payload)

    # JSONPlaceholder accepts incomplete payloads.
    assert response.status_code == 201
    assert response.json()["userId"] == 1


def test_get_post_with_invalid_id_returns_404(api_client):
    with pytest.raises(requests.HTTPError) as exc_info:
        api_client.get("/posts/999999")

    assert exc_info.value.response.status_code == 404