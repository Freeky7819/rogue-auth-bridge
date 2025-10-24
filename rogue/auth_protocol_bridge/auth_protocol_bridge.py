# auth_protocol_bridge.py
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Mapping, Optional

class AuthType(str, Enum):
    MCP = "mcp"
    A2A = "a2a"

@dataclass(frozen=True)
class MCPAuthCredentials:
    token: str

@dataclass(frozen=True)
class A2AAuthCredentials:
    passport: str

def _validate_nonempty(name: str, value: Optional[str]) -> None:
    if not value or not isinstance(value, str):
        raise ValueError(f"{name} must be a non-empty string")

def build_auth_headers(
    auth_type: AuthType | str,
    credentials: MCPAuthCredentials | A2AAuthCredentials | Mapping[str, str],
    extra: Optional[Mapping[str, str]] = None,
) -> Dict[str, str]:
    at = AuthType(str(auth_type).lower())
    base: Dict[str, str] = {}
    if at is AuthType.MCP:
        token = getattr(credentials, "token", None) if not isinstance(credentials, Mapping) else credentials.get("token")
        _validate_nonempty("token", token)
        base["Authorization"] = f"Bearer {token}"
    elif at is AuthType.A2A:
        passport = getattr(credentials, "passport", None) if not isinstance(credentials, Mapping) else credentials.get("passport")
        _validate_nonempty("passport", passport)
        base["x-agent-passport"] = str(passport)
    else:
        raise ValueError(f"Unsupported auth_type: {auth_type}")

    if extra:
        base.update(dict(extra))
    return base

def merge_headers(existing: Optional[Mapping[str, str]], auth_headers: Mapping[str, str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if existing:
        out.update(dict(existing))
    out.update(dict(auth_headers))
    return out
