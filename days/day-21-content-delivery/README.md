# Day 21 — Content Delivery Agent

## Objective

Build an AI-powered publishing agent that reads Markdown content, validates it, logs into a CMS, creates a draft, retrieves the preview URL, and generates a publishing summary.

---

## Features

- Markdown ingestion
- Content formatting
- Validation pipeline
- CMS abstraction layer
- Draft publishing
- Preview URL extraction
- AI-generated publishing summary

---

## Architecture

Markdown
↓
Formatter
↓
Validator
↓
CMS Adapter
↓
Publishing Workflow
↓
Preview Extraction
↓
Publishing Report

---

## Learning Outcomes

- Content automation
- CMS abstractions
- Publishing workflows
- Adapter design pattern
- Browser automation
- Workflow orchestration

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
   - The script loads a dummy markdown file `sample.md` (which you can populate with actual content).
   - The agent prepares the draft and navigates to the CMS editor.
   - It delegates interaction to the `CMSAdapter` which programmatically fills the title and body and saves the draft.
   - The LLM receives the completion status and provides a summary.

---

## Future Improvements

- Image uploads
- SEO metadata generation
- Tag/category automation
- Scheduled publishing
- Multi-CMS support
- Publish vs Draft modes