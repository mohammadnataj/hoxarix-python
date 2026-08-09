from hoxarix import Client


client = Client(
    api_key="YOUR_API_KEY"
)


result = client.runtime.run(
    agent_id="assistant",
    input="Explain AI governance"
)


print(result)
