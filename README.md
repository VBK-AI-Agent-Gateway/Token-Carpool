# 🚀 TokenHub Local Agent

> **TokenHub 本地接入客户端 | Smart-BYOK 智能优化引擎 | P2P 令牌共享网络**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-green?logo=windows&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?logo=mit&logoColor=white)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)]()

---

## ✨ 核心卖点

- 🎯 **通用兼容**：适配所有主流 AI 编程智能体（Cline, Continue.dev, Aider, CodeGPT, Cursor 等）
- ⚡ **零配置**：下载即用，无需修改任何配置文件
- 📦 **单文件**：单个 `.exe` 文件，无依赖，无环境要求
- 🖥️ **托盘运行**：系统托盘后台静默运行，不干扰开发工作流
- 🔄 **无缝接入**：本地端口透明代理到 TokenHub 智能网关

---

## 📖 项目简介

**TokenHub Local Agent** 是 [TokenHub](http://www.agentgwapi.online:8888) 平台的本地接入客户端。它运行在 Windows 系统托盘，通过本地反向代理将你的 AI 编程工具连接到 TokenHub 云端网关。

### TokenHub 平台能力

| 能力 | 说明 |
|------|------|
| **Smart-BYOK 引擎** | L1 归一化 → L2 上下文折叠 → Dual-Mode 约束 → 语义缓存，综合 Token 节省 **38%** |
| **P2P 令牌共享网络** | 实时点对点闲置额度匹配，端到端加密，自动计费结算 |
| **模型矩阵** | Claude Opus 4.1 / Sonnet 4.5 / Haiku 4.5、GPT-4o / 4o mini，统一调度 |
| **供应商网络** | 接入即获流量，免费接入、透明分成、快速上线 |

> **让每一个 Token 都发挥最大价值。** 无需安装 Python 环境，无需配置环境变量——**下载、运行、连接，三步完成。**

---

## 🚀 快速开始

### 1. 下载

从 [Releases](https://github.com/VBK-AI-Agent-Gateway/Token-Carpool/releases) 页面下载最新版本。

### 2. 运行

双击 `TokenHubAgent.exe`，程序将自动在系统托盘启动。

### 3. 连接

在你的 AI 编程智能体中，将 API 端点设置为：

```
http://127.0.0.1:8899
```

**完成！** 所有请求将通过本地客户端代理到 TokenHub 智能优化网关，自动应用 BYOK 压缩优化和缓存命中。

---

## 🛠️ 功能列表

| 功能 | 说明 |
|------|------|
| **本地反向代理** | 将 AI 客户端请求透明转发到 TokenHub 云端网关 |
| **系统托盘** | 最小化至托盘，后台持续运行 |
| **零配置** | 内置默认代理目标，开箱即用 |
| **多客户端适配** | 兼容 Cline、Continue.dev、Aider、CodeGPT、Cursor 等 |
| **单文件部署** | PyInstaller 打包，无外部依赖 |

---

## 🔧 配置说明

### 默认配置

程序启动后默认监听本地端口 `8899`，代理目标为 TokenHub 网关：

```
http://154.12.86.206:8888
```

### 自定义配置（可选）

通过环境变量自定义：

```bash
# 修改代理目标
set PROXY_TARGET=http://www.agentgwapi.online:8888

# 修改本地端口
set PROXY_PORT=8899
```

> 💡 **提示**：对于绝大多数用户，**无需修改任何配置**。

---

## 🖥️ 与各 AI 客户端集成指南

### Cline

1. 打开 Cline 设置
2. 将 API Base URL 设置为 `http://127.0.0.1:8899`
3. 保存并重启 Cline

### Continue.dev

1. 打开 `~/.continue/config.yaml`
2. 修改 `apiBase` 字段为 `http://127.0.0.1:8899`
3. 重启 Continue

### Aider

```bash
aider --api-base http://127.0.0.1:8899
```

### CodeGPT

1. 打开 CodeGPT 设置
2. 将 API Endpoint 设置为 `http://127.0.0.1:8899`

### Cursor

1. 打开 Cursor 设置
2. 在 API 配置中设置 Base URL 为 `http://127.0.0.1:8899`

> 📌 **通用规则**：任何支持自定义 API 端点的 AI 客户端，只需将端点指向 `http://127.0.0.1:8899` 即可。

---

## 🏗️ 构建说明

### 环境要求

- Python 3.8+
- Windows 10/11

### 依赖安装

```bash
pip install -r requirements.txt
```

### 打包

```bash
# 方式一：使用 build.bat
build.bat

# 方式二：使用 build.py
python build.py
```

打包完成后，`dist/` 目录下生成可执行文件。

---

## 📂 项目结构

```
Token-Carpool/
├── main.py              # 主程序源码（126行）
├── build.py             # 打包脚本
├── build.bat            # Windows 一键打包脚本
├── requirements.txt     # Python 依赖
├── README.md            # 项目文档
├── SECURITY.md          # 安全策略
└── dist/                # 打包输出目录（生成后出现）
```

---

## 🌐 相关链接

- **TokenHub 入口**：http://www.agentgwapi.online:8888
- **落地页**：http://154.12.86.206:80
- **GitHub 组织**：https://github.com/VBK-AI-Agent-Gateway

---

## 🇬🇧 English Overview

**TokenHub Local Agent** is the on-premises client for the [TokenHub](http://www.agentgwapi.online:8888) BYOK optimization and P2P token sharing platform. It runs as a single-file Windows executable in the system tray, providing a transparent local proxy that connects your AI coding tools (Cline, Continue.dev, Aider, CodeGPT, Cursor, etc.) to the TokenHub smart gateway. No Python environment, no dependency installation, no config file editing — just works.

TokenHub delivers **up to 38% token cost reduction** through its Smart-BYOK optimization engine (L1 normalization, L2 context folding, dual-mode constraint, semantic caching) and a **P2P token sharing network** for real-time idle quota matching.