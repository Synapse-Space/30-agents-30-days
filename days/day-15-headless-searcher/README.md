# Day 15 — Headless Search Agent

## Objective

Build an autonomous search agent capable of querying the web, extracting text content from the returned pages, and generating a cohesive research summary using a local LLM.

---

## Features

- Headless browser automation via Playwright
- Bypassing of Google CAPTCHAs by leveraging Wikipedia's Search API
- Automated DOM manipulation and script/style tag stripping
- Clean Markdown extraction from scraped pages
- Local LLM summarization via Ollama integration

---

## Architecture

Search Query
↓
Search Engine (Wikipedia)
↓
Playwright Page Extractor
↓
Markdown Builder
↓
Ollama Summarization Prompt
↓
Research Summary

---

## Usage

1. **Install Dependencies:** (Ensure Playwright browsers are installed)
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. **Run the Agent:**
   ```bash
   python main.py
   ```

3. **Interact:**
   - The CLI will prompt you for a "Search Query >".
   - Enter your research topic (e.g., "Agentic AI Frameworks").
   - The agent will invisibly open a headless browser, execute the search, extract the top 3 results, compile them into Markdown, and pass them to Ollama for a final summary.