# tests/test_auth_bridge.py
import unittest
from rogue.auth_protocol_bridge import (
    AuthType, build_auth_headers, merge_headers,
    MCPAuthCredentials, A2AAuthCredentials
)

class TestAuthBridge(unittest.TestCase):
    def test_mcp_headers_with_dataclass(self):
        headers = build_auth_headers(AuthType.MCP, MCPAuthCredentials(token="abc123"))
        self.assertEqual(headers.get("Authorization"), "Bearer abc123")

    def test_mcp_headers_with_mapping(self):
        headers = build_auth_headers("mcp", {"token": "t-1"})
        self.assertEqual(headers.get("Authorization"), "Bearer t-1")

    def test_mcp_token_required(self):
        with self.assertRaises(ValueError):
            build_auth_headers("mcp", {"token": ""})

    def test_a2a_headers_with_dataclass(self):
        headers = build_auth_headers(AuthType.A2A, A2AAuthCredentials(passport="p.jwt"))
        self.assertEqual(headers.get("x-agent-passport"), "p.jwt")

    def test_a2a_headers_with_mapping(self):
        headers = build_auth_headers("a2a", {"passport": "signed.jwt"})
        self.assertEqual(headers.get("x-agent-passport"), "signed.jwt")

    def test_a2a_passport_required(self):
        with self.assertRaises(ValueError):
            build_auth_headers("a2a", {"passport": ""})

    def test_merge_auth_overrides_existing(self):
        user = {"Authorization": "Bearer WRONG", "X-Other": "1"}
        auth = {"Authorization": "Bearer RIGHT"}
        merged = merge_headers(user, auth)
        self.assertEqual(merged["Authorization"], "Bearer RIGHT")
        self.assertEqual(merged["X-Other"], "1")

if __name__ == "__main__":
    unittest.main()
