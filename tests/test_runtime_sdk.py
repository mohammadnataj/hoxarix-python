from hoxarix import Client


def test_runtime_call():

    client = Client(
        api_key="YOUR_API_KEY",
        base_url="http://127.0.0.1:8000"
    )

    result = client.runtime.run(
        agent_id="sdk-test",
        input="Explain AI architecture"
    )

    assert result["success"] is True
    assert "result" in result
