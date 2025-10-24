# 🧩 Rogue Auth Protocol Bridge  
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)

**Unified authentication headers for Rogue evaluator agents.**  
This module enables agents to communicate securely with other MCP and A2A agents that require protocol-level authentication.

---

## 🌐 Overview

Rogue supports multiple communication protocols (MCP, A2A).  
Some remote agents require authorization headers — e.g. `Bearer` tokens or signed `x-agent-passport` credentials.  
This bridge unifies those cases under a single clean interface.

| Protocol | Header | Source |
|-----------|---------|--------|
| **MCP (Model Context Protocol)** | `Authorization: Bearer <token>` | [MCP Basic/Auth Spec](https://modelcontextprotocol.io/specification/draft/basic/authorization) |
| **A2A (Agent-to-Agent)** | `x-agent-passport: <signed-jwt>` | [A2A Authenticated Endpoints](https://a2aprotocol.ai/docs/guide/a2a-samples-hello-world#authenticated-endpoints) |

---

## ⚙️ Installation

```powershell
git clone https://github.com/Freeky7819/rogue-auth-bridge.git
cd rogue-auth-bridge
python -m unittest
🧠 Usage Example
python
Copy code
from rogue.auth_protocol_bridge import build_auth_headers, merge_headers, AuthType

# MCP: Bearer token
hdrs = build_auth_headers(AuthType.MCP, {"token": "abc123"})
# -> {"Authorization": "Bearer abc123"}

# A2A: Signed JWT / passport
hdrs = build_auth_headers(AuthType.A2A, {"passport": "<signed.jwt>"})
# -> {"x-agent-passport": "<signed.jwt>"}

# Merge with existing headers (auth takes precedence)
final = merge_headers({"Accept": "application/json"}, hdrs)
🔄 Integration with Rogue Evaluator
When the evaluator agent calls another authenticated agent:

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
➡️ This layer can live in rogue/server/ or rogue_sdk/utils/,
so the TUI only passes auth_type + credentials, and the evaluator injects the correct headers automatically.

🧪 Demo
Run the included demo to preview header generation:

powershell
Copy code
python demo_auth_handshake.py
It prints both MCP and A2A header sets and their curl equivalents.

✅ Tests
All functionality is covered by unittests:

powershell
Copy code
python -m unittest
📜 License
Licensed under the Apache-2.0 license.
© 2025 Damjan Žakelj

🤝 Acknowledgements
Built as an interoperability layer for the Qualifire Rogue ecosystem.
Fully aligned with:

MCP Basic/Auth specification

A2A protocol authenticated endpoints

Authy v4 / ISM-X passport signing framework

Maintainer: @Freeky7819
PRs and improvements are welcome 
