import os

from hoxarix import Client
from hoxarix import HoxarixAuthenticationError


def test_missing_api_key():

    old_key = os.environ.pop(
        "HOXARIX_API_KEY",
        None
    )

    try:

        try:
            Client(
                api_key=None,
                base_url="http://127.0.0.1:8000"
            )

        except HoxarixAuthenticationError:
            return

        assert False, "Authentication error was not raised"

    finally:

        if old_key:
            os.environ["HOXARIX_API_KEY"] = old_key
