# Security Policy

## Reporting a Vulnerability

We take the security of TokenHub and its local agent seriously. If you discover a security vulnerability, please report it via:

- **Email**: support@agentgwapi.online
- **GitHub Security Advisory**: https://github.com/VBK-AI-Agent-Gateway/Token-Carpool/security/advisories/new

**Please do not** disclose security vulnerabilities in public issues.

## Supported Versions

We commit to acknowledging security reports within **72 hours** and providing a fix or mitigation within **7 days**.

## TokenHub Security Architecture

| Layer | Protection |
|-------|-----------|
| **API Key Storage** | Encrypted at rest with AES-256-GCM, never logged in plaintext |
| **Transport** | All traffic TLS 1.3 between local agent and TokenHub gateway |
| **P2P Sharing** | End-to-end encryption; Keys never leave your local environment |
| **Authentication** | Bearer token authentication via OpenAI-compatible schema |

## Best Practices

1. **Official sources only**: Download binaries only from GitHub Releases.
2. **Verify integrity**: Check SHA-256 hash of downloaded files.
3. **Stay updated**: Regularly update to the latest version.
4. **Least privilege**: Run with normal user permissions, not administrator.

## Known Limitations

- The local agent does **not encrypt** traffic on `127.0.0.1`. This is inherently safe as traffic never leaves the machine.
- Communication between the local agent and the remote TokenHub gateway relies on the gateway's TLS configuration.

## Disclaimer

This software is provided "as is", without warranty of any kind. Users assume all risks associated with its use.

---

*Last updated: 2026*