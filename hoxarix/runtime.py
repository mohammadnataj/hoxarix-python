import requests

from .exceptions import (
    HoxarixAuthenticationError,
    HoxarixConnectionError,
    HoxarixRuntimeError,
)


class RuntimeClient:
    """
    Hoxarix Runtime API Client
    """

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int = 30
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "hoxarix-python-sdk/0.1.2"
        }


    def run(
        self,
        agent_id: str,
        input: str
    ):
        """
        Execute Hoxarix Runtime.
        """

        url = f"{self.base_url}/api/v1/runtime/run"

        payload = {
            "agent_id": agent_id,
            "input": input
        }


        try:
            response = requests.post(
                url,
                json=payload,
                headers=self.headers,
                timeout=self.timeout
            )

        except requests.exceptions.RequestException as e:
            raise HoxarixConnectionError(
                str(e)
            )


        if response.status_code == 401:
            raise HoxarixAuthenticationError(
                "Invalid API key"
            )


        if response.status_code >= 400:
            raise HoxarixRuntimeError(
                response.text
            )


        return response.json()
