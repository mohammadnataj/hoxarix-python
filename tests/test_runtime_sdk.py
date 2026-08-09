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

    assert result["status"] == "completed"
    assert result["error"] is None
    assert "memory" in result
    assert "trace" in result
