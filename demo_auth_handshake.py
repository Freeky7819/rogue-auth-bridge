# demo_auth_handshake.py
from __future__ import annotations
from rogue.auth_protocol_bridge import build_auth_headers, AuthType, merge_headers

def demo_mcp(url: str, token: str):
    auth = build_auth_headers(AuthType.MCP, {"token": token})
    headers = merge_headers({"Accept": "application/json"}, auth)
    print("[MCP] URL:", url)
    print("[MCP] Headers:", headers)
    print("curl -H 'Accept: application/json' -H 'Authorization: {}' '{}'".format(headers["Authorization"], url))

def demo_a2a(url: str, passport: str):
    auth = build_auth_headers(AuthType.A2A, {"passport": passport})
    headers = merge_headers({"Content-Type": "application/json"}, auth)
    print("[A2A] URL:", url)
    print("[A2A] Headers:", headers)
    print("curl -X POST -H 'Content-Type: application/json' -H 'x-agent-passport: {}' '{}'".format(headers["x-agent-passport"], url))

if __name__ == "__main__":
    demo_mcp("https://agent.example.com/mcp/hello", "test-token-123")
    demo_a2a("https://agent.example.com/a2a/hello-world", "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9...")
