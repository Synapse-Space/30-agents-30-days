# Day 11 — Deterministic FAQ Guardrail Agent

## Objective

Build a hybrid AI assistant that answers known business questions deterministically and only uses the LLM for unknown queries.

---

## Features

- FAQ routing
- Guardrail architecture
- RapidFuzz similarity matching
- LLM fallback
- Unknown question logging
- Local Ollama support
- Production-ready routing pattern

---

## Flow

User

↓

FAQ Matcher

↓

Matched?

├── Yes → FAQ Answer
└── No → LLM

---

## Learning Outcomes

- Guardrails
- Hybrid AI
- Rule-Based Routing
- Fuzzy Matching
- Confidence Thresholds
- Cost Optimization
- Production AI Design

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
   - **Known Queries** (e.g., "how can i reset my password?"): Answered instantly by the FAQ.
   - **Unknown Queries** (e.g., "how to create a new account?"): Sent to the LLM and logged to `unknown_questions.json` for review.

---

## Example

Question

↓

What are your refund policies?

↓

FAQ

↓

Deterministic Answer

---

Question

↓

Explain Neural Radiance Fields.

↓

LLM (Also logs question to `unknown_questions.json`)