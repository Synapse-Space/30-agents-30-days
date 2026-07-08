# Day 13 — Customer Support Routing Agent

## Objective

Build an AI-powered customer support assistant that detects customer frustration, adjusts its communication style, and escalates conversations when necessary.

---

## Features

- Rule-based emotion detection
- Dynamic prompt selection
- Escalation engine
- Mock ticket generation
- Emotion-aware responses
- Ollama integration
- Production-inspired architecture

---

## Flow

Customer Message

↓

Emotion Analyzer

↓

Escalation Decision

├── Normal → Friendly Response

└── Escalated → Empathetic Response + Ticket

---

## Learning Outcomes

- Emotion-aware AI
- Sentiment analysis
- Human-in-the-loop workflows
- Dynamic prompting
- Separation of business logic and LLM reasoning

---

## Future Improvements

- Transformer-based sentiment analysis
- Real ticketing integrations (Jira, Zendesk, Freshdesk)
- Confidence calibration
- Multi-language emotion detection
- Historical customer context

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
   - **Normal Query** (e.g., "Hi, I forgot my password."): The agent responds with a friendly, standard support style.
   - **Angry Query** (e.g., "I've been trying this for 3 days! This is terrible!"): The emotion analyzer detects frustration, generates a mock ticket, and switches to an empathetic response mode.