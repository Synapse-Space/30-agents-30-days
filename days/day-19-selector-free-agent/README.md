# Day 19 — Selector-Free Browser Agent

## Objective

Build an AI-powered browser agent that can locate and interact with webpage elements using visual understanding instead of CSS selectors.

---

## Features

- Screenshot-based UI understanding
- Vision LLM element detection
- Candidate ranking
- Coordinate-based mouse interaction
- Action verification
- Recovery strategy
- AI-generated reasoning

---

## Architecture

Browser
↓
Screenshot
↓
Vision Model
↓
Candidate Elements
↓
Planner
↓
Executor
↓
Verifier
↓
Recovery
↓
LLM Explanation

---

## Learning Outcomes

- Vision-guided automation
- Coordinate-based interaction
- Action planning
- Verification patterns
- Recovery strategies
- Computer-use foundations

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

3. **Interact:**
   - The CLI will prompt you for a `URL >`. Provide any webpage URL (e.g. `https://example.com`).
   - The CLI will then prompt you for an `Instruction >`. Describe the UI element you want it to interact with (e.g. `click the submit button`).
   - Playwright will load the page, capture a screenshot, pass it to your local Ollama vision model (`qwen3-vl:latest`), calculate bounding-box coordinates, execute the action, and then verify the change. If the action fails, the agent will attempt to gracefully recover or explain why the target could not be found.

---

## Future Improvements

- Keyboard interaction
- Drag-and-drop support
- Multi-step task execution
- OCR integration
- Desktop application automation
- Autonomous workflow execution