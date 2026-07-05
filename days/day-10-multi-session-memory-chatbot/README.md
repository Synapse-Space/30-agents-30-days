# Day 10 - Multi-Session Memory Chatbot

## Objective

Build a chatbot capable of remembering user facts across multiple application sessions using PostgreSQL.

---

## Features

- Long-term memory
- PostgreSQL persistence
- Memory extraction
- Memory retrieval
- Prompt augmentation
- Structured LLM outputs
- Local Ollama support

---

## Architecture

User

↓

Conversation

↓

Memory Extraction

↓

PostgreSQL

↓

Memory Retrieval

↓

Prompt Augmentation

↓

LLM

↓

Response

---

## Learning Outcomes

- Persistent Memory
- Repository Pattern
- PostgreSQL Integration
- Prompt Augmentation
- Long-Term Personalization
- Context Injection

---

## Example

Session 1

User:

My favorite editor is VS Code.

↓

Memory Stored

---

Session 2

User:

What's my favorite editor?

↓

Assistant:

Your favorite editor is VS Code.