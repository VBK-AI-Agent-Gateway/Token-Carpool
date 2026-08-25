# Token Carpool Security Model

## Overview

Token Carpool handles sensitive API keys from multiple providers. Security is our highest priority.

## Key Security Guarantees

### 1. API Key Protection

- All API keys encrypted at rest using AES-256
- Keys are never logged or exposed in API responses (only last 4 characters shown)
- Zero-knowledge architecture - the platform processes requests without exposing raw keys
- Automatic key rotation support

### 2. Provider Isolation

- Each seller's keys are strictly isolated
- Keys are never shared between different users or stores
- Per-key rate limiting prevents abuse
- Quota management per seller account

### 3. Network Security

- All internal services bound to 127.0.0.1 (no direct external access)
- nginx reverse proxy with rate limiting (per-IP)
- Request sanitization and validation
- CORS and CSP headers configured

### 4. Data Security

- SQLite WAL mode with atomic transactions
- Regular database backups
- No PII stored beyond email and hashed passwords (bcrypt)
- GDPR-aligned data handling

### 5. Operational Security

- Admin endpoints protected by role-based access control (RBAC)
- Separate admin and user authentication tokens
- Audit logging for all key management operations
- Automatic token disable on quota exhaustion

## Architecture Security

```
Internet -> nginx (8888, rate limiting)
         -> Token Carpool Gateway (localhost only)
         -> Provider Router (localhost only)
         -> External AI Providers
```

All backend services are only accessible via localhost. The nginx reverse proxy is the single entry point, enforcing:
- IP-based rate limiting
- Request size limits
- Path-based routing
- SSL termination (when configured)

## Reporting Vulnerabilities

If you discover a security vulnerability, please report it responsibly:

- **Email**: support@agentgwapi.online
- **Do not** open a public GitHub issue for security vulnerabilities
- We aim to respond within 48 hours

---

*Last updated: August 2026*
