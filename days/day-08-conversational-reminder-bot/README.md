# Day 8 - Conversational Reminder Bot

## Objective

Build a conversational AI assistant that remembers previous messages, asks follow-up questions when information is incomplete, and schedules reminders.

---

## Features

- Multi-turn conversations
- Conversation memory
- Structured extraction
- Reminder scheduling
- Background worker
- Persistent reminder storage
- Local Ollama support

---

## Architecture

User

↓

Conversation Memory

↓

LLM

↓

Reminder Extraction

↓

Scheduler

↓

Reminder Store

↓

Background Worker

↓

Reminder Notification

---

## Learning Outcomes

- Conversational AI
- Short-term Memory
- Context Management
- Background Processing
- Multi-turn Dialogues
- Information Extraction
- AI + Traditional Software Engineering

---

## Example

User:

Remind me to call John tomorrow.

↓

Assistant:

What time tomorrow?

↓

User:

5 PM

↓

Reminder Scheduled

↓

🔔 Reminder Triggered