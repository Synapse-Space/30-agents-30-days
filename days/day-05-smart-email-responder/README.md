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