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

LLM