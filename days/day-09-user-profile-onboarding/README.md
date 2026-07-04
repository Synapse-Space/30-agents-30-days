# Day 9 — User Profile Onboarding Agent

## Objective

Build a workflow-driven AI agent that collects user profile information through a strict, validated onboarding process.

---

## Features

- Workflow-driven conversation
- Sequential data collection
- Input validation
- Retry on invalid input
- Profile generation
- Rich CLI interface
- Local Ollama support

---

## Workflow

```text
START
   │
   ▼
Full Name
   │
   ▼
Email
   │
   ▼
Phone
   │
   ▼
Country
   │
   ▼
Profile Complete
```

---

## Learning Outcomes

- Finite State Machines (FSM)
- Workflow-driven AI Agents
- Deterministic Validation
- Sequential User Onboarding
- Conversation + Workflow Integration
- Enterprise AI Design Patterns

---

## Example

```text
Assistant:
What is your full name?

↓

User:
Yuvraj Singh

↓

Assistant:
What is your email address?

↓

User:
yuvraj@gmail.com

↓

Profile Created
```