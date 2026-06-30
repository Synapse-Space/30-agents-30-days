# Day 5 - Smart Email Assistant

## Objective

Build an AI agent that understands emails instead of simply responding to them.

The agent:

- Detects intent
- Estimates priority
- Detects sentiment
- Summarizes the email
- Drafts a professional reply

---

## Workflow

Incoming Email

↓

Structured Agent

↓

LLM

↓

Validated JSON

↓

Business Object

↓

Draft Reply

---

## Features

- Local Ollama
- Structured Outputs
- Pydantic Validation
- Retry Mechanism
- Intent Classification
- Sentiment Analysis
- Reply Generation

---

## Sample Output

```json
{
    "intent": "support",
    "priority": "high",
    "sentiment": "negative",
    "confidence": 0.98,
    "summary": "Customer reports activation issue.",
    "draft_response": "Hi..."
}
```

---

## Learning Outcomes

- Multi-task prompting
- Intent classification
- Structured AI outputs
- Human-in-the-loop readiness
- Enterprise email automation

---

## Folder Structure

```
day-05-smart-email-responder/
├── agent.py           # The EmailAssistantAgent integrating the prompt and LLM call
├── main.py            # Terminal interface using 'rich' for an interactive prompt
├── sample_emails.py   # Collection of sample emails mapping to various intents
└── schemas.py         # Pydantic models (e.g. EmailResponse) for structuring LLM output
```

*Note: This project relies on `shared_core/agents/structured_agent.py` and `shared_core/prompts/email.py` to seamlessly parse and validate the LLM's JSON and provide the core prompt.*

---

## Setup & Running

1. **Activate the Environment:**
   Ensure you are running within the project's virtual environment.
   ```bash
   source ../../venv/bin/activate
   ```

2. **Run the Agent:**
   Launch the main interactive query loop.
   ```bash
   python main.py
   ```