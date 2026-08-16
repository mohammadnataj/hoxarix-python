import os

import pytest

from hoxarix import Client


pytestmark = pytest.mark.integration


def test_render_runtime_call():
    api_key = os.getenv("HOXARIX_API_KEY")
    base_url = os.getenv(
        "HOXARIX_BASE_URL",
        "https://hoxarix-api.onrender.com"
    )

    if not api_key:
        pytest.skip(
            "HOXARIX_API_KEY is not set"
        )

    client = Client(
        api_key=api_key,
        base_url=base_url
    )

    result = client.runtime.run(
        agent_id="integration-test",
        input="Explain Hoxarix runtime architecture"
    )

    assert result["success"] is True
    assert result["error"] is None
    assert "request_id" in result
    assert "result" in result
    assert "trace" in result["result"]
    assert "memory_count" in result["result"]
