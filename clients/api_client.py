import logging
import requests
import time


logger = logging.getLogger(__name__)


class ApiClient:
    """Reusable HTTP client for API automation tests."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)

    
   
    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
    
        start_time = time.perf_counter()
    
        logger.info("Sending %s %s", method, url)
    
        try:
            response = self.session.request(
                method=method,
                url=url,
                **kwargs,
            )
    
            duration = time.perf_counter() - start_time
    
            logger.info(
                "%s %s -> %s (%.3fs)",
                method,
                url,
                response.status_code,
                duration,
            )
    
            response.raise_for_status()
    
            return response
    
        except requests.RequestException:
            logger.exception("Request failed: %s %s", method, url)
            raise


    def close(self):
        self.session.close()