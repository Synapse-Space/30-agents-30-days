# Day 04 — Intelligent SQL Query Builder

## Goal

Convert natural language into safe, read-only SQL queries and execute them against a database.

---

## Workflow

Natural Language

↓

Database Schema

↓

LLM

↓

SQL

↓

Validation

↓

SQLite

↓

Results

---

## Features

- Uses local Ollama
- Structured Outputs
- Pydantic
- Automatic schema loading
- SQL safety validation
- Read-only execution
- Retry mechanism

---

## Folder Structure

```
day-04-sql-query-builder/
├── agent.py           # The SQLAgent running the generation, validation, and execution loop
├── database.py        # Database execution wrapper
├── main.py            # Terminal interface using 'rich' for formatting tables and explanations
├── prompts.py         # System prompt with instructions for the LLM
├── sample_db.py       # Script to generate a mock SQLite database (`sample.db`)
├── schema.py          # Pydantic models (e.g. SQLQuery) for structuring LLM output
└── sql_validator.py   # Guardrails validating safety of SQL (blocks INSERT, UPDATE, etc.)
```

*Note: This project relies on `shared_core/agents/structured_agent.py` to seamlessly parse and validate the LLM's JSON.*

---

## Code Walkthrough

- **`main.py`**: A clean terminal UI using the `rich` library. It takes a user's natural language question, passes it to the `SQLAgent`, prints the LLM's explanation, and displays the resulting database rows in a formatted table.
- **`agent.py`**: Contains `SQLAgent`, inheriting from `StructuredAgent`. It injects the database schema dynamically via `SchemaLoader.as_prompt()`, and validates the generated SQL using `SQLValidator`.
- **`sql_validator.py`**: A strict guardrail mechanism. It ensures the query is a `SELECT` statement and explicitly blocks keywords like `INSERT`, `DROP`, `UPDATE`, `DELETE`, etc.
- **`sample_db.py`**: A setup script that initializes `sample.db` with dummy `users` and `products` tables.
- **`schema.py`**: Defines the `SQLQuery` Pydantic model dictating the expected output from the LLM (an `sql` query string and an `explanation` string).

---

## Setup & Running

1. **Initialize the Database:**
   First, run the `sample_db.py` script to generate the `sample.db` SQLite file.
   ```bash
   python sample_db.py
   ```

2. **Run the Agent:**
   Launch the main interactive query loop.
   ```bash
   python main.py
   ```

---

## Example

**You >** How many users are there?

**Generated SQL**

```sql
SELECT COUNT(*) AS total_users
FROM users;
```

**Result**

```
42
```

---

## Lessons Learned / Outcomes

- **Structured AI Outputs**: Using Pydantic to strictly type the LLM's returned SQL and explanation.
- **SQL Safety**: Using a deterministic parser/regex block list (`sql_validator.py`) to prevent destructive actions by the agent.
- **Prompt Grounding**: Injecting the live database schema (DDL) directly into the prompt so the LLM doesn't hallucinate tables.
- **Database Schema Injection**: Automatically reading sqlite metadata to stay in sync with database changes.
- **Agent Design**: Combining reasoning (LLM) with hardcoded safety guardrails (Python).