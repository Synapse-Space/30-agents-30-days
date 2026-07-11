# Day 17 — Authenticated Profile Analyzer

## Objective

Build an AI-powered browser agent that restores an authenticated session, extracts structured profile information from an authorized profile page, and generates intelligent insights.

---

## Features

- Persistent Playwright storage state
- Authenticated browser sessions
- Structured profile extraction
- Profile metrics analysis
- AI-generated profile insights
- Reusable authentication framework

---

## Architecture

Storage State
↓
Authentication Manager
↓
Browser Context
↓
Profile Extraction
↓
Metrics Analysis
↓
LLM Summary

---

## Learning Outcomes

- Session persistence
- Browser context management
- Authenticated automation
- Structured data extraction
- Business rule analysis
- AI-assisted reporting

---

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. **Authenticate (Optional):**
   - Populate `storage_state.json` with valid LinkedIn session cookies to scrape actual profiles.
   - If unauthenticated, the agent will gracefully fail over to placeholder data and proceed with AI generation.

3. **Run the Agent:**
   ```bash
   python main.py
   ```

4. **Interact:**
   - The CLI will prompt you for a "Profile URL >".
   - Enter a LinkedIn profile link.
   - It will extract the profile details, compute professional network metrics, and use Ollama to generate an analytical summary.

---

## Future Improvements

- Multi-platform profile adapters
- Profile trend tracking
- Engagement history
- PDF report generation
- Dashboard visualizations
- Scheduled profile audits