# Day 27 — Self-Healing Error Recovery Worker

## 📌 Overview & Objective

Day 27 implements an autonomous **Self-Healing Error Recovery Worker** designed to handle runtime failures in background task execution. When a task encounters an exception, rather than crashing silently or failing permanently, the system:
1. Captures the exception and stack trace via an `ErrorAnalyzer`.
2. Invokes an LLM-assisted `OllamaRepairEngine` to diagnose the root cause and generate a repaired payload.
3. Automatically retries execution up to a configured threshold (`RetryPolicy`), throwing `RetryLimitExceeded` if maximum retry attempts are exhausted.

---

## 🛠️ Tech Stack & Dependencies

- **Worker Framework**: Celery + Redis broker task queuing
- **Agent Architecture**: `RecoveryAgent` inheriting from `SelfHealingWorkerAgent` & `BaseAgent`
- **Recovery Pipeline**: `shared_core.recovery` (`ErrorAnalyzer`, `RetryPolicy`, `RepairEngine`, `SelfHealingWorker`)
- **LLM Diagnostic Engine**: Ollama (`llama3.1:latest`) via `langchain_ollama`
- **Terminal UI**: `rich` formatted panels and tables

---

## 🏗️ Architecture & Data Flow

```text
Task Submitted ──► Celery Task Queue ──► Redis Broker
                                                │
                                                ▼
                                     Self-Healing Worker
                                                │
                                   ┌────────────┴────────────┐
                                   ▼                         ▼
                             (Task Success)           (Task Failure)
                                   │                         │
                                   ▼                         ▼
                             Job Completed            Error Analyzer
                                                             │
                                                             ▼
                                                 LLM Repair Engine (Ollama)
                                                             │
                                               ┌─────────────┴─────────────┐
                                               ▼                           ▼
                                        (Retry < Limit)          (Retry Limit Reached)
                                    Retry with Fixed Payload      RetryLimitExceeded
```

---

## 🚀 How to Run

### 1. Prerequisites
- Ensure Redis is running locally on port 6379 (or Celery fallback mode).
- Ensure Ollama is running locally with `llama3.1:latest`:
  ```bash
  ollama pull llama3.1:latest
  ```

### 2. Execution
Navigate to the Day 27 directory and run `main.py`:

```bash
cd days/day-27-self-healing-worker
python3 main.py
```

### 3. Example Interaction & Output

```text
╭─────── Recovery Pipeline ────────╮
│ Self-Healing Worker              │
│ Day 27 • 30 AI Agents in 30 Days │
╰──────────────────────────────────╯
                  Task Submitted                  
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric  ┃ Value                                ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Task ID │ c44a4b4a-806e-4995-ab5a-bf65cab86f92 │
│ Status  │ queued                               │
└─────────┴──────────────────────────────────────┘

╭─────────────────────────────── Execution Flow ───────────────────────────────╮
│ If the task fails, the worker will analyze the exception, ask the LLM for a  │
│ repair, and retry automatically.                                             │
╰──────────────────────────────────────────────────────────────────────────────╯
```

---

## 🎯 Key Learnings & Features

- **Autonomous Error Handling**: Intercepts task exceptions and prevents unnecessary escalation.
- **LLM-Assisted Payloads**: Uses local LLMs to repair invalid input data or payloads dynamically.
- **Bounded Retry Loops**: Enforces max attempt limits to prevent infinite execution loops.
- **Resilient AI Pipelines**: Builds production-ready background workers capable of self-remediation.