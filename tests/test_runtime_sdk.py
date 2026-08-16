from hoxarix import Client


def test_runtime_call():

    client = Client(
        api_key="hooshix-dev-key",
        base_url="http://127.0.0.1:8000"
    )

    result = client.runtime.run(
        agent_id="sdk-test",
        input="Explain AI architecture"
    )

    assert result["success"] is True
    assert result["error"] is None
    assert "result" in result
    assert "memory_count" in result["result"]
    assert "trace" in result["result"]
