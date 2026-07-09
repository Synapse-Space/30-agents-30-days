# Day 14 — Code Review Assistant

## Objective

Build a Python code review assistant that combines deterministic AST-based analysis with AI-generated explanations.

---

## Features

- Python AST parsing
- Static rule engine
- Function & class inspection
- Quality scoring
- AI-generated recommendations
- Ollama integration

---

## Architecture

Python File

↓

AST Parser

↓

AST Visitor

↓

Rule Engine

↓

Review Findings

↓

LLM

↓

Review Report

---

## Learning Outcomes

- Abstract Syntax Trees (AST)
- Static analysis
- Rule-based validation
- Prompt engineering
- AI-assisted developer tooling

---

## Future Improvements

- Cyclomatic complexity analysis
- Security rules
- PEP 8 style checks
- Duplicate code detection
- Automated refactoring suggestions

---

## Usage

1. **Install Dependencies:** (Done in project root)
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Agent:**
   ```bash
   python main.py
   ```
3. **Interact:**
   - The script will prompt you for a file to review: `Python file to review: `
   - Enter a path to a Python script (e.g., `sample_code/bad.py` or `sample_code/good.py`).
   - The Code Review Assistant will parse the file's AST, run static rules, and then feed the report to the local LLM to generate an actionable human-readable code review with a final Quality Score.