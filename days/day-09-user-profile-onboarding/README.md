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

---

## Folder Structure

```text
day-09-user-profile-onboarding/
├── agent.py               # OnboardingAgent implementing the FSM workflow
├── main.py                # Interactive CLI loop
├── models.py              # Pydantic data models for the User Profile
├── prompts.py             # System prompts for the agent
├── sample_input.py        # Example inputs for testing
├── validators.py          # Validation logic for email, phone, etc.
└── workflow.py            # FSM (Finite State Machine) state definitions
```

*Note: This day utilizes the `shared_core` library—specifically `shared_core.agents.workflow_agent` and `shared_core.workflow`, which provide the base classes for finite state machines.*

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
   Launch the interactive onboarding workflow.
   ```bash
   python main.py
   ```