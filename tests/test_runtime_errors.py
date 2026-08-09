import pytest

from hoxarix import Client
from hoxarix import (
    HoxarixAuthenticationError,
    HoxarixConnectionError,
)


def test_invalid_api_key():

    client = Client(
        api_key="wrong-key",
        base_url="http://127.0.0.1:8000"
    )

    with pytest.raises(HoxarixAuthenticationError):
        client.runtime.run(
            "security-test",
            "invalid key test"
        )


def test_connection_error():

    client = Client(
        api_key="YOUR_API_KEY",
        base_url="http://127.0.0.1:9999",
        timeout=2
    )

    with pytest.raises(HoxarixConnectionError):
        client.runtime.run(
            "connection-test",
            "server unavailable"
        )
