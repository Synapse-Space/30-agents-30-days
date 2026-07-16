# Day 20 — Workflow Automation Agent

## Objective

Build an AI-powered workflow agent that reads structured CSV data, maps it to a browser form, executes a multi-step submission workflow, validates each step, and generates a completion report.

---

## Features

- CSV data ingestion
- Configurable field mapping
- Workflow planning
- Multi-step execution
- Validation handling
- Recovery strategy
- AI-generated execution summary

---

## Architecture

CSV
↓
Field Mapper
↓
Workflow Planner
↓
Queue
↓
Executor
↓
Validator
↓
Recovery
↓
Report

---

## Learning Outcomes

- Workflow orchestration
- State management
- Queue-based execution
- Data mapping
- Validation handling
- Enterprise automation design

---

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. **Run the Agent:**
   ```bash
   python main.py
   ```

3. **Execution Flow:**
   - The script loads sample automation targets from `sample_data.csv`.
   - The agent maps the target fields into a strict multi-step plan.
   - It executes each step (e.g. typing in "First Name", then "Last Name") securely using the `WorkflowQueue`.
   - After clicking "Submit Form", the LLM evaluates the state and prints a summary.

---

## Future Improvements

- Multi-page workflows
- Dynamic field detection
- Vision-based validation
- Parallel workflow execution
- Retry policies with backoff
- Audit logging