# Day 03 — Structured Data Extractor

## Goal

Learn how to use Pydantic to strictly enforce data extraction formats, ensuring LLMs return perfectly structured JSON that maps directly to typed objects.

---

## Concepts

- Pydantic Models & Field Validation
- Structured JSON Extraction
- Retry & Self-Correction Loops
- Exception Handling with LLMs

---

## Architecture

(User / Unstructured Text)

↓

(LLM) — *Prompted to extract specific fields*

↓

(Raw Text Output)

↓

(JSON Parser)

↓

(Pydantic Validator)

↓

(Success: Returns Validated Object) OR (Failure: Loops back to LLM with Error Message)

---

## Folder Structure

```
day-03-structured-data-extractor/
├── agent.py           # The StructuredExtractorAgent that manages the extraction loop
├── main.py            # Terminal interface using 'rich' for pretty printing
├── prompts.py         # SYSTEM_PROMPT containing extraction rules
├── sample_emails.py   # Dummy emails for testing extraction
└── schemas.py         # Pydantic BaseModels (e.g. ContactInformation)
```
*Note: This project relies on `shared_core/json_parser.py` and `shared_core/validator.py` to decouple the parsing and validation logic from the specific agent.*

---

## Code Walkthrough

- **`main.py`**: A beautiful terminal UI built with the `rich` library. It lets the user choose between preset sample emails or enter a custom one, then prints out the final structured JSON extraction.
- **`agent.py`**: Contains the `StructuredExtractorAgent` which inherits from `BaseAgent`. It runs a `while` loop up to `MAX_RETRIES`. If the Pydantic validation fails, it catches the `ValidationError` and appends a new message telling the LLM exactly *what* failed so the LLM can self-correct in the next iteration.
- **`schemas.py`**: Defines a `ContactInformation` Pydantic class. This dictates exactly what fields (like `name`, `email`, `phone_number`) are expected, acting as a rigid schema contract. 
- **`shared_core/json_parser.py`**: Safely parses the raw text from the LLM, catching `JSONDecodeError` if the model hallucinates non-JSON text.
- **`shared_core/validator.py`**: Runs the parsed JSON through the Pydantic model's `model_validate` method, ensuring all data types and required fields are present.

---

## Lessons Learned

- **Enforced Schemas**: Asking an LLM for JSON isn't enough; you must validate the schema. Pydantic is the industry standard for this in Python.
- **LLM Self-Correction**: When an LLM fails to match a schema, you don't necessarily have to crash. You can feed the stack trace or validation error *back* into the LLM as a user message, and models are surprisingly good at fixing their own mistakes!
- **Data Pipelines**: Transforming unstructured data (like raw emails) into structured data (like JSON or database rows) is one of the most powerful and immediate use cases for Agentic pipelines.

---

## Challenge

Modify `schemas.py` to add a new required field: `meeting_date` of type `str` (or `datetime` if you're brave). Test it on `Sample Email #1` to see if the LLM successfully pulls out "next Tuesday at 3 PM".

---

## Next Day Preview

Tomorrow we will build an Intelligent SQL Query Builder that reflects on database schemas and adds prompt guardrails for safe execution!
