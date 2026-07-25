# Day 28 — Dual-Core Dialogue Hybrid

## 📌 Overview & Objective

Day 28 implements a **Dual-Core Dialogue Hybrid Assistant** designed to seamlessly bridge the gap between deterministic business form workflows and open-ended LLM reasoning.

In enterprise conversational systems:
- **Rasa Engine**: Handles structured business actions (e.g., bank account creation, loan applications, KYC data collection).
- **LangGraph Engine**: Handles open-ended Q&A, conceptual explanations, and side questions using local LLM reasoning (Ollama `llama3.1:latest`).

The **Hybrid Router** dynamically evaluates user intents and conversation state, allowing users to ask side questions mid-form without losing their place in the business workflow.

---

## 🛠️ Tech Stack & Dependencies

- **Routing & Pipeline**: `HybridRouter`, `EnterprisePipeline`, `ConversationState` (`shared_core.dialogue`)
- **Business Workflow Engine**: `EnterpriseRasaEngine` (multi-step form state management)
- **Reasoning Engine**: `EnterpriseLangGraph` backed by Ollama (`llama3.1:latest`)
- **LLM Engine**: `langchain_ollama`
- **Terminal UI**: `rich` formatted tables and panels

---

## 🏗️ Architecture & Data Flow

```text
User Input
    │
    ▼
Hybrid Router (router.py)
    │
    ├─────────────────────────────────────────┐
    ▼ (Business Form Intent)                  ▼ (Conceptual Q&A)
Rasa Engine (rasa_engine.py)             LangGraph Engine (langgraph_engine.py)
    │                                         │
    ├─► Form State Management                 ├─► Multi-Turn History Context
    ├─► Step 1: Full Name                     └─► Ollama (llama3.1:latest) LLM Response
    ├─► Step 2: Email
    └─► Application Submission
    │                                         │
    └────────────────────┬────────────────────┘
                         ▼
                Unified Response & Shared State
```

---

## 🚀 How to Run

### 1. Prerequisites
- Ensure Ollama is running locally with `llama3.1:latest`:
  ```bash
  ollama pull llama3.1:latest
  ```

### 2. Execution
Navigate to the Day 28 directory and run `main.py`:

```bash
cd days/day-28-dual-core-dialogue
python3 main.py
```

### 3. Example Interaction

```text
You > how to open a bank account

        Routing         
┏━━━━━━━━━━┳━━━━━━━┓
┃ Property ┃ Value ┃
┡━━━━━━━━━━╇━━━━━━━┩
│ Engine   │ rasa  │
└──────────┴───────┘

Assistant: [Rasa Workflow] Starting Bank Account Application.
           Step 1/2: Please enter your Full Name:

You > what is the difference between savings and current account?

        Routing         
┏━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Property ┃ Value     ┃
┡━━━━━━━━━━╇━━━━━━━━━━━┩
│ Engine   │ langgraph │
└──────────┴───────────┘

Assistant: [LangGraph Reasoning] A savings account is designed for saving money and earning interest...

You > Yuvraj Singh

        Routing         
┏━━━━━━━━━━┳━━━━━━━┓
┃ Property ┃ Value ┃
┡━━━━━━━━━━╇━━━━━━━┩
│ Engine   │ rasa  │
└──────────┴───────┘

Assistant: [Rasa Workflow] Thank you, Yuvraj Singh.
           Step 2/2: Please enter your Email Address:
```

---

## 🎯 Key Learnings & Features

- **Intent Precedence Routing**: Question patterns (`"what is"`, `"explain"`, `"difference"`, `"why"`, `"how"`) take precedence to prevent Q&A queries from being misrouted to form fields.
- **Context-Aware Multi-Turn History**: `LangGraphEngine` and `RasaEngine` record and maintain history (`state.history`) for context-aware LLM follow-ups.
- **Enterprise Form Filling**: Stateful slot collection (`full_name`, `email`) with automatic form reset upon completion.
- **Seamless Engine Handoff**: Interleave structured forms with open-ended Q&A without breaking session context.