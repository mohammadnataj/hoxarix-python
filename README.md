# Hoxarix Python SDK

Official Python SDK for Hoxarix AI Runtime Infrastructure.

Created by Mohammad Hasan Nataj Ansar.

Hoxarix provides a runtime layer for building reliable AI agents with runtime execution, policy-aware decisions, explainable responses, and secure API access.

## Installation

Install the SDK:

pip install hoxarix

## Authentication

Create an API key from your Hoxarix developer account.

Set environment variable:

export HOXARIX_API_KEY="your_api_key"

Or pass directly:

from hoxarix import Client

client = Client(
    api_key="YOUR_API_KEY"
)

## Quick Start

from hoxarix import Client

client = Client(
    api_key="YOUR_API_KEY"
)

result = client.runtime.run(
    agent_id="assistant",
    input="Explain AI governance"
)

print(result)

## Runtime API

The SDK connects to:

POST /api/v1/runtime/run

Example request:

{
  "agent_id": "assistant",
  "input": "Hello"
}

## Configuration

HOXARIX_API_KEY:
API authentication key

HOXARIX_BASE_URL:
Custom Runtime API endpoint

## Error Handling

Available exceptions:

HoxarixError

HoxarixAuthenticationError

HoxarixConnectionError

HoxarixRuntimeError

## Examples

examples/quickstart.py

## Development

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest

## Version

0.1.2

## Author

Mohammad Hasan Nataj Ansar

Creator of Hoxarix AI Runtime Infrastructure.

## License

Apache License 2.0
