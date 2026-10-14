import time
import pytest
import requests

from clients.api_client import ApiClient

from utils.assertions import (assert_status_code, assert_json_contains,)


BASE_URL = "https://jsonplaceholder.typicode.com"


def api_client():
    """Provide a reusable HTTP session for API tests."""
    with requests.Session() as session:
        yield session


def test_get_existing_post_returns_200(api_client):
    response = api_client.get("/posts/1")
    assert_status_code(response, 200)


def test_post_response_contains_required_fields():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert_status_code(response, 200)
    assert_json_contains(
        response,
        ["userId", "id", "title", "body"],
    )


@pytest.mark.parametrize("post_id", [1, 2, 3, 10, 50])
def test_post_has_expected_id(api_client, post_id):
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=10,
    )

    assert_status_code(response, 200)
    assert response.json()["id"] == post_id


def test_nonexistent_post_returns_404():
    response = requests.get(
        f"{BASE_URL}/posts/999999",
        timeout=10,
    )

    assert_status_code(response, 404)


@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_post_title_is_not_empty(api_client, post_id):
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=10,
    )

    assert_status_code(response, 200)
    assert response.json()["title"].strip() != ""


def test_api_response_time_is_reasonable():
    start = time.perf_counter()

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=10,
    )

    elapsed = time.perf_counter() - start

    assert_status_code(response, 200)
    assert elapsed < 3.0, (
        f"Response took {elapsed:.2f} seconds"
    )