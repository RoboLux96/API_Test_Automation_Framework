import logging
import os

import pytest

from clients.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    base_url = os.getenv(
        "API_BASE_URL",
        "https://jsonplaceholder.typicode.com",
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    client = ApiClient(base_url=base_url)

    yield client

    client.close()