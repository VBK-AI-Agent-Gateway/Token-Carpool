# Security Policy

## Reporting a Vulnerability

Report via: **support@agentgwapi.online** or [GitHub Advisory](https://github.com/VBK-AI-Agent-Gateway/Token-Carpool/security/advisories/new)

## Architecture Security

| Layer | Protection |
|-------|-----------|
| **Local Agent** | Runs on `127.0.0.1` — traffic never leaves machine |
| **Gateway Transport** | TLS 1.3 between agent and `api.tokenhub.work` |
| **API Keys** | Encrypted at rest (AES-256-GCM), never logged |
| **Self-Host Mode** | Full control — your keys, your network |

## Best Practices

- Download binaries only from **GitHub Releases**
- Self-host via Docker for maximum privacy
- Verify SHA-256 checksums on downloaded files
- Run with normal user permissions (not admin)

## Disclaimer

Provided "as is", without warranty. Users assume all risks.

---

*Last updated: 2026*