# Hoxarix Python SDK

**Official Python SDK for Hoxarix — an AI Runtime Infrastructure and Control Layer.**

Hoxarix sits between an AI application or agent and model execution, providing a runtime layer for **controlled, observable, and governed AI execution**.

> Hoxarix is not a chatbot framework.

## 🧠 What is Hoxarix?

Modern AI applications often send requests directly from an application or agent to an underlying model. Hoxarix introduces a runtime layer between those two sides so that requests can be evaluated and governed before execution.

```text
Application / Agent
        ↓
   Hoxarix Runtime
        ↓
Intent + Risk Analysis
        ↓
 Policy Enforcement
  ALLOW / MODIFY / BLOCK
        ↓
 Memory / Runtime State
        ↓
 Model / LLM Execution
        ↓
 Trace / Explainability
```

Hoxarix is designed to provide runtime infrastructure for:

- 🛡️ Policy enforcement and governance
- 🔎 Intent and risk analysis
- 🧠 Contextual memory and runtime state
- 🔐 Controlled API access
- 📋 Runtime trace and explainability
- 📊 Observable AI execution

The Python SDK is the simplest developer-facing way to connect a Python application or agent to the Hoxarix Runtime.

## 🚀 Why use the Python SDK?

Use the SDK when you want to put Hoxarix in the execution path of an application or agent without implementing the Runtime API integration yourself.

The SDK handles the client-side connection to the Hoxarix Runtime and exposes a simple Python interface:

```python
result = client.runtime.run(
    agent_id="assistant",
    input="Explain AI governance in one sentence."
)
```

The underlying Runtime evaluates the request and returns the normalized runtime response.

## 📦 Current Release

**Hoxarix Python SDK v0.1.4**

GitHub Release:

https://github.com/mohammadnataj/hoxarix-python/releases/tag/v0.1.4

The SDK uses the Hoxarix production Runtime API by default:

```text
https://api.hoxarix.com
```

For custom deployments, the base URL can be overridden with `HOXARIX_BASE_URL`.

## 🔑 Get Developer Access

To use the Hoxarix Runtime API, create a developer account at:

https://hoxarix.com/developer

After signing in:

1. Create an API key.
2. Copy the secret when it is shown.
3. Store it securely.
4. Use it through the `HOXARIX_API_KEY` environment variable.

Never commit your API key to Git or place it directly in public source code.

## ⚡ Installation

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

## 🔐 Authentication

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

## 🎯 Quick Start

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

## 🌐 Runtime API

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

A successful runtime response can include normalized execution and governance information such as:

```text
status
intent
risk_score
confidence
policy
pipeline
memory
trace
```

Depending on the request and runtime policy, Hoxarix may allow, modify, or block execution.

## 🛡️ Runtime Governance

The SDK connects your application to a runtime that can evaluate requests before downstream model execution.

Conceptually:

```text
Request
  ↓
Intent / Risk Analysis
  ↓
Policy Enforcement
  ├── ALLOW
  ├── MODIFY
  └── BLOCK
  ↓
Runtime Execution
```

Hoxarix includes deterministic rule-based protections for recognized risky patterns. These controls are designed to prevent recognized requests from reaching downstream execution; they are not a claim of universal attack prevention.

## 🌐 REST / cURL

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

## ⚙️ Configuration

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

## 🚨 Error Handling

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

## 📚 Examples

Example code is available in:

```text
examples/quickstart.py
```

## 🧩 Repository Role

This repository is the **public Python developer interface** for Hoxarix.

```text
Hoxarix Core
Private
        ↓
Hoxarix Website / Developer Console
Private
        ↓
Hoxarix Python SDK
Public
```

The implementation details of the Hoxarix Runtime and the Website remain in their respective private repositories. This repository focuses on helping developers integrate with Hoxarix.

## 🛠️ Development

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

## 📌 Version

```text
0.1.4
```

## 👤 Author

**Mohammad Hassan Nataj Ansar**

Creator of Hoxarix AI Runtime Infrastructure.

## 📄 License

Apache License 2.0
