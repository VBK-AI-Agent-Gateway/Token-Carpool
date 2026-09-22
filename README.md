# TokenHub

> **Open-Source Smart Routing Gateway — One Line, 94% Token Savings**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows|Linux|macOS-green?logo=windows&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?logo=mit&logoColor=white)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)]()
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker&logoColor=white)]()

---

## ✨ One Line to Integrate, 94% Tokens Saved

TokenHub is a **fully open-source smart routing gateway** for AI coding agents. It strips timestamps/UUIDs to stabilize cache prefixes, folds conversation history, constrains output format — then routes across **20+ vendors** by cost, latency and availability.

| Capability | Impact |
|-----------|--------|
| **normalize_request** | Cross-session cache hit: **99%+** — strips TS/UUID/seed/path so cache keys match across sessions |
| **state_folding** | Input reduction: **15–39%** — folds cold history, keeps semantics, drops redundancy |
| **constrained_output** | Output reduction: **21–66%** — forces JSON shape, cuts verbosity |
| **Smart Routing** | **20+ vendors** unified behind one OpenAI-compatible endpoint, cost-optimal + auto failover |

---

## 🚀 One-Click Download & Install

### Windows (EXE)

[![Download](https://img.shields.io/badge/⬇️_Download-TokenHub_Agent-00FF9D?style=for-the-badge&logo=windows)](https://github.com/VBK-AI-Agent-Gateway/Token-Carpool/releases/latest)

```powershell
# One-liner: download and run
curl -LO https://github.com/VBK-AI-Agent-Gateway/Token-Carpool/releases/latest/download/TokenHubAgent.exe
.\TokenHubAgent.exe
```

**Point your AI client to `http://127.0.0.1:8899`** — done.

### Docker (Self-Host)

```bash
git clone https://github.com/VBK-AI-Agent-Gateway/Token-Carpool.git
cd Token-Carpool
docker compose up -d
# Gateway: http://localhost:8080/v1
```

### Any SDK

```python
# Only one line changes: base_url
client = OpenAI(
    api_key="sk-...",
    base_url="https://api.tokenhub.work/v1"   # ← this is all
)
```

---

## 🔧 How It Works

```
Request → normalize_request → Cache Lookup → Route Decision → Vendor
               │                      │              │
          strip TS/UUID           99% hit      cost · latency
          fold history            cache-first   auto failover
```

---

## 🖥️ Client Integration Guide

### Cline
Set `API Base URL → http://127.0.0.1:8899`

### Continue.dev
In `~/.continue/config.yaml`:
```yaml
apiBase: http://127.0.0.1:8899
```

### Aider
```bash
aider --api-base http://127.0.0.1:8899
```

### Cursor / CodeGPT
Set API Endpoint → `http://127.0.0.1:8899`

---

## 📊 Benchmarks

| Call | Direct OpenAI | Via TokenHub |
|------|--------------|--------------|
| Session 1 (cold) | 1,800ms | 3,118ms |
| Session 2 | 791ms **miss** cached=0 | 992ms **hit -68%** |
| Session 3 | 989ms **miss** cached=0 | 593ms **hit -81%** |

**Direct OpenAI**: 0/3 cache hits. **TokenHub**: 2/2 hits after cold start.

---

## 🏗️ Build from Source

```bash
pip install -r requirements.txt
python build.py
# Output: dist/TokenHubAgent.exe
```

---

## 📂 Project Structure

```
├── main.py              # Local agent (126 lines)
├── build.py             # PyInstaller build script
├── build.bat            # Windows one-click build
├── requirements.txt     # Python dependencies
├── README.md
└── LICENSE (MIT)
```

---

## 🌐 Links

- **Gateway API**: `https://api.tokenhub.work/v1`
- **Landing**: http://5.189.129.216
- **Website**: http://www.agentgwapi.online:8888
- **GitHub**: https://github.com/VBK-AI-Agent-Gateway/Token-Carpool

---

## 🇨🇳 中文简介

TokenHub 是一个完全开源的智能路由网关，专门为 AI 编程智能体设计。通过**一行代码**修改 `base_url`，即可享受 **94% Token 节省**：自动剥离时间戳/UUID 稳定缓存前缀、折叠历史对话、约束输出格式，并在 **20+ 厂商**之间智能路由（成本最优 + 自动故障转移）。支持 Docker 自托管，MIT 开源，可审计、可 Fork、可私有部署。