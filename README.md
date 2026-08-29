# Hoxarix Python SDK

Official Python SDK for **Hoxarix AI Runtime Infrastructure**.

Hoxarix provides an AI runtime control layer for building reliable AI agents with:

* Runtime execution
* Policy enforcement
* Governance controls
* Explainability
* Observability
* Memory protection
* Secure API access

## Current Release

**Hoxarix Python SDK v0.1.4**

GitHub Release:

https://github.com/mohammadnataj/hoxarix-python/releases/tag/v0.1.4

The SDK uses the Hoxarix production Runtime API by default:

```text
https://api.hoxarix.com
```

For custom deployments, the base URL can be overridden with `HOXARIX_BASE_URL`.

## Get Developer Access

To use the Hoxarix Runtime API, create a developer account at:

https://hoxarix.com/developer

After signing in:

1. Create an API key.
2. Copy the secret when it is shown.
3. Store it securely.
4. Use it through the `HOXARIX_API_KEY` environment variable.

Never commit your API key to Git or place it directly in public source code.

## Installation

The official SDK is currently distributed through **GitHub Releases**.

Download the latest v0.1.4 release from:

https://github.com/mohammadnataj/hoxarix-python/releases/tag/v0.1.4

Then install the wheel:

```bash
pip install hoxarix-0.1.4-py3-none-any.whl
```

You can also install the source distribution:

```bash
pip install hoxarix-0.1.4.tar.gz
```

## Authentication

Set your API key as an environment variable.

### Linux / macOS

```bash
export HOXARIX_API_KEY="your_api_key"
```

### Windows PowerShell

```powershell
$env:HOXARIX_API_KEY="your_api_key"
```

The SDK reads the API key automatically.

You can also pass the key directly:

```python
from hoxarix import Client

client = Client(
    api_key="YOUR_API_KEY"
)
```

## Quick Start

```python
import os
from hoxarix import Client

client = Client(
    api_key=os.environ["HOXARIX_API_KEY"]
)

result = client.runtime.run(
    agent_id="assistant",
    input="Explain AI governance in one sentence."
)

print(result)
```

The SDK uses:

```text
https://api.hoxarix.com
```

by default, so no `HOXARIX_BASE_URL` setting is required for the public production service.

## Runtime API

The SDK calls the Hoxarix Runtime Contract:

```text
POST /api/v1/runtime/run
```

Production endpoint:

```text
https://api.hoxarix.com/api/v1/runtime/run
```

Example JSON request:

```json
{
  "agent_id": "assistant",
  "input": "Explain AI governance in one sentence."
}
```

## REST / cURL

You can call the Runtime API directly without the Python SDK.

### Linux / macOS

```bash
curl -X POST https://api.hoxarix.com/api/v1/runtime/run \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $HOXARIX_API_KEY" \
  -d '{
    "agent_id": "assistant",
    "input": "Explain AI governance in one sentence."
  }'
```

### Windows PowerShell

```powershell
$headers = @{
    "Content-Type" = "application/json"
    "X-API-Key"    = $env:HOXARIX_API_KEY
}

$body = @{
    agent_id = "assistant"
    input    = "Explain AI governance in one sentence."
} | ConvertTo-Json

Invoke-RestMethod `
    -Method Post `
    -Uri "https://api.hoxarix.com/api/v1/runtime/run" `
    -Headers $headers `
    -Body $body
```

## Configuration

### `HOXARIX_API_KEY`

Your Hoxarix developer API key.

Recommended:

```text
HOXARIX_API_KEY
```

### `HOXARIX_BASE_URL`

Optional custom Runtime API endpoint.

Example:

```bash
export HOXARIX_BASE_URL="https://your-custom-runtime.example.com"
```

When not provided, the SDK uses:

```text
https://api.hoxarix.com
```

## Runtime Results

A successful Runtime request returns the normalized Hoxarix runtime response.

Depending on the request, the response can include runtime and policy information such as:

```text
success
intent
risk_score
confidence
policy
pipeline
```

Example policy decision:

```text
ALLOW
```

Hoxarix can also block requests that violate runtime policy or governance controls.

## Error Handling

The SDK provides typed exceptions including:

```text
HoxarixError
HoxarixAuthenticationError
HoxarixConnectionError
HoxarixRuntimeError
```

Example:

```python
from hoxarix import Client
from hoxarix import HoxarixAuthenticationError

try:
    client = Client(
        api_key="YOUR_API_KEY"
    )

    result = client.runtime.run(
        agent_id="assistant",
        input="Hello"
    )

    print(result)

except HoxarixAuthenticationError:
    print("Authentication failed.")
```

## Examples

Example code is available in:

```text
examples/quickstart.py
```

## Development

Clone the repository:

```bash
git clone https://github.com/mohammadnataj/hoxarix-python.git
cd hoxarix-python
```

Install the project dependencies according to the repository configuration, then run:

```bash
pytest
```

The repository separates standard CI tests from integration and stress tests that require a running Runtime service.

## Version

```text
0.1.4
```

## Author

**Mohammad Hasan Nataj Ansar**

Creator of Hoxarix AI Runtime Infrastructure.

## License

Apache License 2.0
