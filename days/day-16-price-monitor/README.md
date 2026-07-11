# Day 16 — Dynamic Price Monitor

## Objective

Build an autonomous monitoring agent that compares product price snapshots, calculates percentage differences, flags thresholds for alerting, and uses a local LLM to summarize market movements.

---

## Features

- Pydantic models for strict structured data representation
- Automated comparative analysis (price drops and increases)
- Rules-based Alert Engine for immediate notifications
- Integration with local LLM (Ollama) for compiling human-readable summaries
- Modular architecture using shared infrastructure components

---

## Architecture

Previous Snapshot & Current Snapshot
↓
Price Detector (Comparative Engine)
↓
Alert Engine (Threshold Triggers)
↓
Ollama Summarization Prompt
↓
Market Movement Report

---

## Usage

1. **Install Dependencies:** (Ensure you have activated your environment)
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Agent:**
   ```bash
   python main.py
   ```

3. **Interact:**
   - The CLI will read the pre-configured `previous.json` and `current.json` mock data snapshots from `sample_data/`.
   - It will display a rich terminal table with the calculated price differences.
   - It will display any triggered alerts (price increases or decreases).
   - Finally, it will print out the AI-generated summary of the price movements.