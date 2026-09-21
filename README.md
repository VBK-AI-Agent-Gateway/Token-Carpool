# 🚀 Token-Carpool

> **通用反向代理网关客户端 | 零配置 | 单文件 Windows EXE**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-green?logo=windows&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?logo=mit&logoColor=white)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)]()

---

## ✨ 核心卖点

- 🎯 **通用性**：适配所有主流 AI 编程智能体（Cline, Continue.dev, Aider, CodeGPT, Cursor 等）
- ⚡ **零配置**：下载即用，无需修改任何配置文件
- 📦 **单文件**：单个 `.exe` 文件，无依赖，无环境要求
- 🖥️ **托盘运行**：系统托盘后台静默运行，不干扰开发工作流
- 🔄 **反向代理**：将远程 API/网页无缝嵌入本地端口

---

## 📖 项目简介

**Token-Carpool** 是一个轻量级的通用反向代理网关客户端，专为 AI 编程智能体用户设计。它通过本地端口代理远程 API 请求，解决跨域、认证、网络隔离等问题，让任何支持自定义 API 端点的 AI 客户端都能无缝接入。

无需安装 Python 环境，无需配置环境变量，无需修改客户端设置——**下载、运行、连接，三步完成。**

---

## 🚀 快速开始

### 1. 下载

从 [Releases](https://github.com/VBK-AI-Agent-Gateway/Token-Carpool/releases) 页面下载最新版本的 `Token-Carpool.exe`。

### 2. 运行

双击 `Token-Carpool.exe`，程序将自动在系统托盘启动。

### 3. 连接

在你的 AI 编程智能体中，将 API 端点设置为：

```
http://127.0.0.1:8899
```

**完成！** 所有请求将通过本地网关代理到远程服务。

---

## 🛠️ 功能列表

| 功能 | 说明 |
|------|------|
| **反向代理** | 将远程 HTTP/HTTPS 请求转发至本地端口 `8899` |
| **系统托盘** | 最小化至托盘，后台持续运行 |
| **零配置** | 内置默认配置，无需手动编辑 |
| **多客户端适配** | 兼容 Cline、Continue.dev、Aider、CodeGPT、Cursor 等 |
| **单文件部署** | PyInstaller 打包，无外部依赖 |

---

## 🔧 配置说明

### 默认配置

程序启动后默认监听本地端口 `8899`，代理目标为：

```
http://154.12.86.206:8888
```

### 自定义配置（可选）

如需修改代理目标或本地端口，可通过环境变量：

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

1. 启动 Aider 时添加参数：
   ```bash
   aider --api-base http://127.0.0.1:8899
   ```
2. 或在 `~/.aider.conf.yml` 中设置：
   ```yaml
   api_base: http://127.0.0.1:8899
   ```

### CodeGPT

1. 打开 CodeGPT 设置
2. 将 API Endpoint 设置为 `http://127.0.0.1:8899`
3. 保存配置

### Cursor

1. 打开 Cursor 设置
2. 在 API 配置中设置 Base URL 为 `http://127.0.0.1:8899`
3. 重启 Cursor

> 📌 **通用规则**：任何支持自定义 API 端点的 AI 客户端，只需将端点指向 `http://127.0.0.1:8899` 即可。

---

## 📸 截图

| 系统托盘 | AI 客户端配置 |
|:--------:|:------------:|
| ![tray](assets/tray-screenshot.png) | ![config](assets/config-screenshot.png) |

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

打包完成后，`dist/` 目录下将生成 `Token-Carpool.exe`。

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

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源。

---

## 🌐 相关链接

- **入口网站**：http://www.agentgwapi.online:8888
- **落地页**：http://154.12.86.206:80
- **GitHub 组织**：https://github.com/VBK-AI-Agent-Gateway

---

## 🇬🇧 English Overview

**Token-Carpool** is a universal reverse proxy gateway client designed for AI coding agents. It runs as a single-file Windows executable, requiring zero configuration. Simply download, run, and point your AI client (Cline, Continue.dev, Aider, CodeGPT, Cursor, etc.) to `http://127.0.0.1:8899`. The client silently runs in the system tray, proxying all requests to the remote gateway. No Python environment, no dependency installation, no config file editing — just works.