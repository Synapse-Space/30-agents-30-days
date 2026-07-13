# Day 18 — Visual UI Understanding Agent

## Objective

Build an AI-powered browser agent that captures webpage screenshots, detects UI elements using a Vision LLM, calculates interaction coordinates, and explains why the selected element matches the user's request.

---

## Features

- Playwright screenshot capture
- Vision-based UI detection
- Structured UI element parsing
- Bounding box representation
- Coordinate calculation
- AI-generated explanations
- Reusable vision framework

---

## Architecture

Browser
↓
Screenshot
↓
Vision Model
↓
UI Elements
↓
Planner
↓
Coordinates
↓
LLM Explanation

---

## Learning Outcomes

- Vision-capable LLMs
- Screenshot processing
- Bounding-box reasoning
- Coordinate systems
- Visual grounding
- Computer-use architecture

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
   - The CLI will then prompt you for an `Instruction >`. Describe the UI element you want it to find (e.g. `find the main header` or `click the submit button`).
   - Playwright will load the page, capture a screenshot, pass it to your local Ollama vision model (`qwen3-vl:latest`), calculate bounding-box coordinates, and explain the reasoning behind its selection.

---

## Future Improvements

- Multiple target ranking
- OCR integration
- Desktop automation
- Multi-monitor support
- Visual action execution
- Real-time screen streaming