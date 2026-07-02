# Day 7 — FX Sentinel

## Objective

Build a stateful AI agent capable of monitoring live exchange rates and notifying users when configured thresholds are crossed.

---

## Features

- Live exchange rate retrieval
- Persistent state
- Threshold monitoring
- Alert engine
- Rich CLI
- Ollama-ready architecture

---

## Architecture

```text
User
 │
 ▼
FX Sentinel
 │
 ├── Fetch Live Rate
 ├── Load Previous State
 ├── Compare Threshold
 ├── Save Updated State
 └── Display Alert
```

---

## Learning Outcomes

- Stateful AI Agents
- Persistent Storage
- Monitoring Systems
- Rule Engines
- External API Integration
- Context Management

---

## Example

Rule:

```text
USD → INR

Alert Above: 87.50
```

Current Rate:

```text
87.62
```

Output:

```text
ALERT

Threshold Crossed
```