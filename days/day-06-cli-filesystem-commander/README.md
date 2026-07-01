# Day 6 — CLI File-System Commander

## Goal

Build an AI agent capable of safely interacting with the local filesystem.

---

## Features

- Local Ollama
- Tool Calling
- File Creation
- File Reading
- File Writing
- File Deletion
- Directory Creation
- Directory Listing
- Workspace Isolation
- Safety Validation

---

## Architecture

User

↓

LLM

↓

Tool Selection

↓

Safety Validation

↓

Workspace Validation

↓

Tool Execution

↓

Execution Result

---

## Learning Outcomes

- Tool Calling
- ReAct
- Agent Actions
- Pydantic Tool Schemas
- Sandboxed Execution
- Secure File Operations

---

## Folder Structure

```
day-06-cli-filesystem-commander/
├── agent.py               # The FileSystemAgent bridging tools and LLM
├── main.py                # Interactive terminal loop
├── safety.py              # Path traversal and security validation logic
├── sample_commands.py     # Example prompts to test the agent
├── workspace.py           # Ensures operations remain in the local sandbox
└── tools/                 # Tool implementations (create, read, write, delete, etc.)
```

*Note: This day heavily relies on the newly modularized `shared_core` library—specifically `shared_core.agents.tool_agent` and `shared_core.tools`, which provide the base classes for orchestrating multi-step Tool Calling.*

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
   Launch the interactive commander interface.
   ```bash
   python main.py
   ```