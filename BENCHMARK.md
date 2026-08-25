# Token Carpool - Performance Benchmark

## Token Amplification Engine Performance

Real-world production data from the Token Carpool platform (Hong Kong + JD Cloud nodes).

### Layer-by-Layer Savings

| Layer | Technology | Metric | Result |
|---|---|---|---|
| **L1 Normalization** | Request normalization (prefix cache optimization) | Cache hit rate | **93.1%** |
| **L2 Folding** | Cold history compression (ratio threshold 0.15) | Context reduction | **60-85%** |
| **Dual-Mode Output** | Adaptive output constraint injection | Output token savings | **40-70%** |
| **Cache Control** | Intelligent TTL + async warmup | Sustained cache reuse | **75-94%** |
| **Overall** | All layers combined | Total token savings | **Up to 86%** |

### Amplification Factor

With 86% token savings, the effective capacity amplification:

```
Original:  1.0x capacity (raw subscription)
After L1:  1.4x (cache normalization)
After L2:  3.0x (history folding)
After Dual: 4.2x (output optimization)
After Cache: 5.0x (full cache reuse)
```

**Result: 3-5x effective token capacity from the same subscription.**

### Cache Performance Over Time

| Time Window | Cache Hit Rate | Notes |
|---|---|---|
| Per-request (cold) | 47.9% | First interaction |
| Per-session (warm) | 75.3% | After warmup |
| Sustained (1h) | 94.3% | Active session |
| Peak (9th hour) | 98.2% | Maximum observed |

### Latency

| Metric | Value | Notes |
|---|---|---|
| Non-streaming response | 1100ms avg | Down from 2800ms baseline (-60%) |
| Streaming first token | < 500ms | Provider-dependent |
| Failover switchover | < 500ms | Automatic multi-provider routing |
| Cache warmup | Async | Zero impact on user requests |

### Throughput

| Metric | Value |
|---|---|
| Concurrent connections | 20+ per node |
| Rate limit | 10 req/s per IP (nginx) |
| Node capacity | 2C/4G (Hong Kong), scalable |

### Provider Coverage

Tested and verified with 9+ global AI providers:

| # | Provider | Region | Status |
|---|---|---|---|
| 1 | DeepSeek | China | Verified |
| 2 | Anthropic (Claude) | Global | Verified (proxy for HK) |
| 3 | OpenAI (GPT-4o) | Global | Verified (proxy) |
| 4 | Google (Gemini) | Global | Verified |
| 5 | xAI (Grok) | Global | Verified |
| 6 | Alibaba (Qwen) | China | Verified |
| 7 | Zhipu AI (GLM) | China | Verified |
| 8 | MiniMax | China | Verified |
| 9 | Xiaomi (MiMo) | China | Verified |

### Key Technologies

1. **L1 Normalization** (`prefix_cache_optimizer.py`): Strips non-semantic request variations to maximize prefix cache hits
2. **L2 Folding** (`gateway_merged.py`): Compresses cold conversation history into compact markers
3. **Dual-Mode Output** (`output_constraint.py`): Injects output format constraints to reduce unnecessary token generation
4. **Cache Control** (`gateway_merged.py`): Manages ephemeral cache TTL with async warmup workers
5. **Smart Routing** (`rules.json`): Intent classification + multi-provider route resolution
6. **Stream Fix** (`_clean_empty_tool_calls`, `_normalize_tool_delta`): Handles edge cases in tool calling streams

---

*Benchmarks collected from production instances, August 2026. Results may vary based on usage patterns.*
