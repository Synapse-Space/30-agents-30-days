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

---

## Folder Structure

```text
day-10-multi-session-memory-chatbot/
├── agent.py               # MemoryChatbot integrating LLM extraction & memory recall
├── main.py                # Interactive CLI, DB connection & agent instantiation
├── memory_extractor.py    # Interfaces with LLM to extract key-value facts
├── models.py              # Pydantic schema for ExtractedMemory
├── prompts.py             # System instructions & few-shot JSON examples
└── sample_inputs.py       # Example interactions for testing
```

*Note: This agent heavily relies on the `shared_core.memory` package, which houses the repository pattern implementation, Pydantic data models for the database, and the PostgreSQL driver adapter (`psycopg3`).*

---

## Setup & Running

1. **Database Setup:**
   Ensure your local PostgreSQL or Docker equivalent (`ai-memory-db`) is running and the database `ai_agents` exists. 
   Apply the memory schema (from the project root):
   ```bash
   psql postgresql://postgres:postgres@localhost:5432/ai_agents -f shared_core/agents/schema.sql
   ```

2. **Python Environment:**
   Ensure `shared_core` is installed and `psycopg` is available:
   ```bash
   source ../../venv/bin/activate
   pip install psycopg[binary]
   # if you haven't already: pip install -e .
   ```

3. **Run the Application:**
   Enter an arbitrary User ID to start a session. Any facts stated will persist across application restarts for that specific ID!
   ```bash
   python main.py
   ```