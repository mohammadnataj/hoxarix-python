import os

from .runtime import RuntimeClient
from .exceptions import HoxarixAuthenticationError


class Client:
    """
    Main Hoxarix SDK Client
    """

    SDK_VERSION = "0.1.3"

    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        timeout: int = 30
    ):

        self.api_key = (
            api_key
            or os.getenv("HOXARIX_API_KEY")
        )

        self.base_url = (
            base_url
            or os.getenv(
                "HOXARIX_BASE_URL",
                "https://hoxarix-api.onrender.com"
            )
        )

        self.timeout = timeout


        if not self.api_key:
            raise HoxarixAuthenticationError(
                "Missing Hoxarix API key. "
                "Set HOXARIX_API_KEY environment variable."
            )


        self.runtime = RuntimeClient(
            api_key=self.api_key,
            base_url=self.base_url,
            timeout=self.timeout
        )


    def version(self):
        """
        Return SDK version.
        """

        return {
            "sdk": f"Hoxarix Python SDK {self.SDK_VERSION}",
            "api": "Hoxarix Runtime API v2"
        }
