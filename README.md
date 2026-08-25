<div align="center">

# Token Carpool

### Global Idle API Token Sharing Platform

**Share idle subscription tokens. Amplify 3-5x. Ultra-low prices worldwide. Zero downtime.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Cloud--Native-green.svg)]()
[![Amplification](https://img.shields.io/badge/Token_Amplification-3--5x-orange.svg)]()
[![Uptime](https://img.shields.io/badge/Uptime-99.9%25-brightgreen.svg)]()
[![GitHub Stars](https://img.shields.io/github/stars/VBK-AI-Agent-Gateway/Token-Carpool?style=social)]()

[English](#english) | [Chinese](#chinese)

</div>

---

## <a name="english"></a>What is Token Carpool?

**Token Carpool** is the world's first **AI Token Sharing Economy Platform**.

You pay $200/month for Claude, DeepSeek, or GPT subscriptions but only use 40% of your tokens. The remaining 60% goes to waste.

**Token Carpool changes everything.**

We invented a proprietary **Token Amplification Engine** that can multiply your idle subscription tokens by **3-5x** before selling them on the platform. Your wasted subscriptions become continuous income. Meanwhile, users worldwide get high-quality AI tokens at prices far below official rates -- a true win-win.

---

## Core Concept

```
Idle Subscriptions -> Token Amplification -> Platform Sharing -> Global Ultra-Low Prices -> Zero Downtime
```

| Pain Point | Token Carpool Solution |
|---|---|
| Personal subscriptions underused, tokens wasted | List idle tokens on the platform, turn waste into revenue |
| Individual site owners want to sell tokens but lack tech skills | **One-click storefront** setup, zero code required |
| Local deployed models can't connect to API sales | **Fast local model integration** (Ollama/vLLM/llama.cpp) with unified sales |
| Users forced to disconnect when tokens run out | **Intelligent fallback system**, zero-interruption global access |
| Official API prices are expensive | Platform shared prices at **20-40% of official rates** |

---

## Platform Architecture

```
+-----------------------------------------------------+
|                Token Carpool Platform                 |
|                                                       |
|  +----------+  +----------+  +------------------+    |
|  | Personal |  |  Team    |  | Local Deployed   |    |
|  | Token    |  |  Token   |  | Models           |    |
|  | Pool     |  |  Pool    |  | (Ollama/vLLM)    |    |
|  +-----+----+  +-----+----+  +--------+---------+    |
|        |              |                |               |
|        +----------+---+----------------+               |
|                   |                                    |
|    +-------------------------------+                  |
|    |   Token Amplification Engine  |                  |
|    |   (Proprietary Technology)    |                  |
|    |                               |                  |
|    |   * Intelligent Compression   |                  |
|    |   * Cache Multiplexing        |                  |
|    |   * Response Folding          |                  |
|    |   * Output Optimization       |                  |
|    +---------------+---------------+                  |
|                    |                                   |
|    +-------------------------------+                  |
|    |   Smart Routing & Fallback    |                  |
|    |                               |                  |
|    |   * Multi-provider routing    |                  |
|    |   * Load balancing            |                  |
|    |   * Auto failover             |                  |
|    |   * Rate limit management     |                  |
|    +---------------+---------------+                  |
|                    |                                   |
|           +--------+--------+                         |
|           |   Global Users   |                         |
|           |  (Ultra-Low Cost)|                         |
|           +------------------+                         |
+-------------------------------------------------------+
```

---

## Key Features

### 1. Token Amplification Engine (Proprietary)

Our core technology uses four layers of optimization to multiply effective token capacity:

| Layer | Technology | Savings |
|---|---|---|
| **L1 Normalization** | Request normalization for maximum cache hit | Up to 93% cache hit rate |
| **L2 Folding** | Cold history compression into compact summaries | 60-85% context reduction |
| **Dual-Mode Output** | Adaptive output constraint injection | 40-70% output token savings |
| **Cache Control** | Intelligent cache TTL management with warmup | 75-94% cache reuse |

**Real-world result: Up to 86% total token savings with 3-5x effective capacity amplification.**

### 2. One-Click Storefront

Individual site owners can launch their own token store in under 60 seconds:

- Register an account
- Connect your API keys (BYOK - Bring Your Own Key)
- Set your pricing
- Start earning immediately

No coding. No server management. No DevOps.

### 3. Local Model Integration

Seamlessly connect locally deployed models to the platform:

- **Ollama** - Direct integration, one command setup
- **vLLM** - High-throughput serving with OpenAI-compatible API
- **llama.cpp** - Lightweight local inference
- **Any OpenAI-compatible API** - Universal connector

Your local models become part of the global token pool.

### 4. Intelligent Fallback System

When one provider goes down or runs out of tokens, the platform automatically routes to the next available provider:

- Multi-provider redundancy across 9+ AI providers
- Automatic failover in under 500ms
- Transparent to end users - zero interruption
- Geographic routing for optimal latency

### 5. Multi-Provider Support

Built-in support for the world's leading AI providers:

| Provider | Models |
|---|---|
| **DeepSeek** | deepseek-v4, deepseek-reasoner |
| **Anthropic** | Claude 3.5 Sonnet, Claude 3 Haiku |
| **OpenAI** | GPT-4o, GPT-4o-mini |
| **Google** | Gemini 2.0, Gemini 1.5 Pro |
| **xAI** | Grok-3, Grok-2 |
| **Alibaba** | Qwen 3.5 Plus, Qwen Turbo |
| **Zhipu AI** | GLM-5.2, GLM-4 |
| **MiniMax** | MiniMax-M3, MiniMax-Text |
| **Xiaomi** | MiMo-v2.5 |

---

## How It Works

### For Token Sellers

```
1. Register          -> Create your seller account
2. Connect Keys      -> Add your API subscriptions (BYOK)
3. Set Pricing       -> Choose your margin
4. Launch Store      -> One-click go live
5. Earn              -> Tokens sold, revenue flows
```

### For Token Buyers

```
1. Browse            -> Find the best token deals
2. Purchase          -> Pay at ultra-low prices
3. Use               -> Same API, same quality, seamless experience
4. Auto-Fallback     -> Zero downtime guaranteed
```

---

## Quick Start

### Register

Visit: [http://www.agentgwapi.online:8888/register](http://www.agentgwapi.online:8888/register)

### API Endpoint

```
Base URL: http://www.agentgwapi.online:8888/v1
```

### OpenAI-Compatible Usage

```python
import openai

client = openai.OpenAI(
    base_url="http://www.agentgwapi.online:8888/v1",
    api_key="your-token-carpool-key"
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### cURL

```bash
curl http://www.agentgwapi.online:8888/v1/chat/completions \
  -H "Authorization: Bearer your-token-carpool-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

## Benchmark

See [BENCHMARK.md](BENCHMARK.md) for detailed performance data.

**Summary:**
- Token amplification: **3-5x** effective capacity
- Cache hit rate: **75-94%** (sustained sessions)
- Total token savings: **Up to 86%**
- API latency: **< 1.5s** (non-streaming)
- Uptime: **99.9%**
- Supported providers: **9+** global AI providers
- Fallback switchover: **< 500ms**

---

## Pricing

Token Carpool operates on a **sharing economy model**:

| Plan | Price | Description |
|---|---|---|
| **Buyer** | 20-40% of official | Access all providers at shared prices |
| **Seller** | Free to list | Earn from your idle tokens |
| **Storefront** | Free | One-click shop setup |

---

## Security

See [SECURITY.md](SECURITY.md) for our security model.

**Key guarantees:**
- All API keys encrypted at rest (AES-256)
- Zero-knowledge key management
- Provider isolation
- Automatic key rotation support
- SOC2-aligned audit logging

---

## <a name="chinese"></a>Token Carpool (Chinese)

### What is Token Carpool?

**Token Carpool** is the world's first **AI Token Sharing Economy Platform**.

You pay $200/month for Claude, DeepSeek, or GPT subscriptions but only use 40% of your tokens. The remaining 60% goes to waste.

**Token Carpool changes everything.**

We invented a proprietary **Token Amplification Engine** that can multiply your idle subscription tokens by **3-5x** before selling them on the platform. Your wasted subscriptions become continuous income. Meanwhile, users worldwide get high-quality AI tokens at prices far below official rates -- a true win-win.

### Core Concept

```
Idle Subscriptions -> Token Amplification -> Platform Sharing -> Global Ultra-Low Prices -> Zero Downtime
```

| Pain Point | Token Carpool Solution |
|---|---|
| Personal subscriptions underused, tokens wasted | List idle tokens on the platform, turn waste into revenue |
| Individual site owners want to sell tokens but lack tech skills | **One-click storefront** setup, zero code required |
| Local deployed models can't connect to API sales | **Fast local model integration** (Ollama/vLLM/llama.cpp) with unified sales |
| Users forced to disconnect when tokens run out | **Intelligent fallback system**, zero-interruption global access |
| Official API prices are expensive | Platform shared prices at **20-40% of official rates** |

### Key Features

**Token Amplification Engine (Proprietary)**: Four-layer optimization -- L1 Request Normalization (93% cache hit), L2 History Folding (60-85% compression), Dual-Mode Output Optimization (40-70% savings), Cache Smart Management (75-94% reuse). Total savings up to 86%, effective amplification 3-5x.

**One-Click Storefront**: Register -> Connect API Key -> Set Price -> Go Live. Zero code, zero ops.

**Local Model Integration**: Supports Ollama / vLLM / llama.cpp / any OpenAI-compatible API.

**Intelligent Fallback**: 9+ global AI providers, auto-failover within 500ms, zero user interruption.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Contact

- **Website**: [http://www.agentgwapi.online:8888](http://www.agentgwapi.online:8888)
- **Register**: [http://www.agentgwapi.online:8888/register](http://www.agentgwapi.online:8888/register)
- **Email**: support@agentgwapi.online

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## Founders

- **Tristan Qin** - Co-Founder & CEO
- **Tomcom Shu** - Co-Founder & CTO
- **Lewis** - Co-Founder & Chief Architect

---

<div align="center">

**Token Carpool** - Share Tokens, Save Money, Earn Together.

*The future of AI token economics.*

</div>
