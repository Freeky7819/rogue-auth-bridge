# 🧩 Rogue Auth Protocol Bridge

**Unified authentication headers for Rogue evaluator agents**  
Seamlessly enables secure agent-to-agent communication using standardized MCP and A2A authentication methods.

---

## 🌐 Overview

Rogue supports multiple communication protocols — **MCP** and **A2A** — where some remote agents require authorization headers.  
This bridge provides a single, unified interface to generate and merge those headers.

| Protocol | Header Example | Reference |
|-----------|----------------|------------|
| **MCP (Model Context Protocol)** | `Authorization: Bearer <token>` | [MCP Basic/Auth Spec](https://modelcontextprotocol.io/specification/draft/basic/authorization) |
| **A2A (Agent-to-Agent)** | `x-agent-passport: <signed-jwt>` | [A2A Authenticated Endpoints](https://a2aprotocol.ai/docs/guide/a2a-samples-hello-world#authenticated-endpoints) |

---

## ⚙️ Installation

```bash
git clone https://github.com/Freeky7819/rogue-auth-bridge.git
cd rogue-auth-bridge
python -m unittest
🧠 Usage Example
python
Copy code
from rogue.auth_protocol_bridge import build_auth_headers, merge_headers, AuthType

# MCP example: Bearer token
hdrs = build_auth_headers(AuthType.MCP, {"token": "abc123"})
# -> {"Authorization": "Bearer abc123"}

# A2A example: Signed JWT / passport
hdrs = build_auth_headers(AuthType.A2A, {"passport": "<signed.jwt>"})
# -> {"x-agent-passport": "<signed.jwt>"}

# Merge with existing headers (auth takes precedence)
final = merge_headers({"Accept": "application/json"}, hdrs)
🧩 Integration with Rogue Evaluator
When the evaluator agent needs to call another authenticated agent:

python
Copy code
from rogue.auth_protocol_bridge import build_auth_headers, merge_headers, AuthType

if config.auth_type == "mcp":
    auth = build_auth_headers(AuthType.MCP, {"token": config.token})
elif config.auth_type == "a2a":
    auth = build_auth_headers(AuthType.A2A, {"passport": config.passport})
else:
    auth = {}

headers = merge_headers(request_headers, auth)
response = requests.post(agent_url, headers=headers, json=payload)
💡 Tip: This layer can live inside rogue/server/ or rogue_sdk/utils/.
The TUI only needs to pass auth_type and credentials — the evaluator handles the rest.

🧪 Demo
Run the included demo to preview header generation:

bash
Copy code
python demo_auth_handshake.py
You’ll see sample output for both MCP and A2A modes, including equivalent curl commands.

✅ Tests
Unit tests ensure correctness and backward compatibility:

bash
Copy code
python -m unittest
All test cases pass locally (AuthType, header merging, error handling).

📜 License
Licensed under the Apache-2.0 License
© 2025 [Freedom (Damjan Žakelj)]

🤝 Acknowledgements
Developed as an interoperability layer for the Qualifire Rogue ecosystem.
Compliant with:

MCP Basic/Auth specification

A2A protocol authenticated endpoints

Authy v4 / ISM-X passport framework

Maintainer: @Freeky7819
Pull Requests and feedback are welcome 🚀# 🧩 Rogue Auth Protocol Bridge

**Unified authentication headers for Rogue evaluator agents**  
Seamlessly enables secure agent-to-agent communication using standardized MCP and A2A authentication methods.

---

## 🌐 Overview

Rogue supports multiple communication protocols — **MCP** and **A2A** — where some remote agents require authorization headers.  
This bridge provides a single, unified interface to generate and merge those headers.

| Protocol | Header Example | Reference |
|-----------|----------------|------------|
| **MCP (Model Context Protocol)** | `Authorization: Bearer <token>` | [MCP Basic/Auth Spec](https://modelcontextprotocol.io/specification/draft/basic/authorization) |
| **A2A (Agent-to-Agent)** | `x-agent-passport: <signed-jwt>` | [A2A Authenticated Endpoints](https://a2aprotocol.ai/docs/guide/a2a-samples-hello-world#authenticated-endpoints) |

---

## ⚙️ Installation

```bash
git clone https://github.com/Freeky7819/rogue-auth-bridge.git
cd rogue-auth-bridge
python -m unittest

🧠 Usage Example
```python
Copy code
from rogue.auth_protocol_bridge import build_auth_headers, merge_headers, AuthType

# MCP example: Bearer token
hdrs = build_auth_headers(AuthType.MCP, {"token": "abc123"})
# -> {"Authorization": "Bearer abc123"}

# A2A example: Signed JWT / passport
hdrs = build_auth_headers(AuthType.A2A, {"passport": "<signed.jwt>"})
# -> {"x-agent-passport": "<signed.jwt>"}

# Merge with existing headers (auth takes precedence)
final = merge_headers({"Accept": "application/json"}, hdrs)
🧩 Integration with Rogue Evaluator
When the evaluator agent needs to call another authenticated agent:

```python
Copy code
from rogue.auth_protocol_bridge import build_auth_headers, merge_headers, AuthType

if config.auth_type == "mcp":
    auth = build_auth_headers(AuthType.MCP, {"token": config.token})
elif config.auth_type == "a2a":
    auth = build_auth_headers(AuthType.A2A, {"passport": config.passport})
else:
    auth = {}

headers = merge_headers(request_headers, auth)
response = requests.post(agent_url, headers=headers, json=payload)
💡 Tip: This layer can live inside rogue/server/ or rogue_sdk/utils/.
The TUI only needs to pass auth_type and credentials — the evaluator handles the rest.

🧪 Demo
Run the included demo to preview header generation:

bash
Copy code
python demo_auth_handshake.py
You’ll see sample output for both MCP and A2A modes, including equivalent curl commands.

✅ Tests
Unit tests ensure correctness and backward compatibility:

bash
Copy code
python -m unittest
All test cases pass locally (AuthType, header merging, error handling).

📜 License
Licensed under the Apache-2.0 License
© 2025 [Damjan Žakelj]

🤝 Acknowledgements
Developed as an interoperability layer for the Qualifire Rogue ecosystem.
Compliant with:

MCP Basic/Auth specification

A2A protocol authenticated endpoints

Authy v4 / ISM-X passport framework

Maintainer: @Freeky7819
Pull Requests and feedback are welcome 🚀
