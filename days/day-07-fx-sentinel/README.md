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

---

## Folder Structure

```text
day-07-fx-sentinel/
├── agent.py               # FXSentinelAgent inheriting from StatefulAgent
├── main.py                # Interactive CLI loop
├── market_provider.py     # Real-time exchange rate API integration
├── alert_engine.py        # Logic to check threshold crossings
├── sample_rules.py        # Configured currency rules
└── storage/
    └── state.json         # Persistent context and market state
```

*Note: This day utilizes the modularized `shared_core` library—specifically `shared_core.agents.stateful_agent` and `shared_core.context`, which provide the base classes for state persistence.*

---

## Setup & Running

1. **Ensure `shared_core` is Installed:**
   Make sure you have run the root `pip install -e .` so the environment can locate `shared_core`.
   ```bash
   source ../../venv/bin/activate
   # If not installed yet, run this from the project root:
   # pip install -e .
   ```

2. **Run the Agent:**
   Launch the interactive Sentinel interface.
   ```bash
   python main.py
   ```