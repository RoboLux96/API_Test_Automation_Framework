import logging
from unittest.mock import patch

import pytest
import requests

from clients.api_client import ApiClient


def test_api_client_raises_timeout(caplog):
    client = ApiClient(
        base_url="https://example.com",
        timeout=10,
    )

    try:
        with patch.object(
            client.session,
            "request",
            side_effect=requests.Timeout("Request timed out"),
        ):
            with caplog.at_level(logging.ERROR, logger="clients.api_client"):
                with pytest.raises(requests.Timeout):
                    client.get("/")

        assert "Request failed: GET https://example.com/" in caplog.text

    finally:
        client.close()


@pytest.mark.parametrize("status_code", [404, 500]) 
def test_api_client_handles_http_error(status_code): 
    client = ApiClient( base_url="https://example.com", timeout=10, ) 
    
    try: 
        mock_response = requests.Response() 
        mock_response.status_code = status_code 
        mock_response.url = "https://example.com/resource" 
        
        with patch.object( client.session, "request", return_value=mock_response, ): 
            response = client.get("/resource") 
            
        assert response.status_code == status_code 
        
    finally: 
        client.close()


@pytest.mark.parametrize("status_code", [404, 500])
def test_api_client_handles_http_error(status_code):
    client = ApiClient(
        base_url="https://example.com",
        timeout=10,
    )

    try:
        mock_response = requests.Response()
        mock_response.status_code = status_code
        mock_response.url = "https://example.com/resource"

        with patch.object(
            client.session,
            "request",
            return_value=mock_response,
        ):
            with pytest.raises(requests.HTTPError) as exc_info:
                client.get("/resource")

        assert exc_info.value.response.status_code == status_code

    finally:
        client.close()