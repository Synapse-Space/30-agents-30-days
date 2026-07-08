# Day 12 – Contextual Document Q&A Agent

## Objective

Build a lightweight document question-answering agent without using embeddings or vector databases.

The agent retrieves relevant document chunks using keyword matching and provides only those chunks as context to the LLM.

---

## Features

- Local document ingestion
- Paragraph-based chunking
- Keyword indexing
- Keyword retrieval
- Context injection
- Prompt augmentation
- Ollama integration
- Framework-ready retrieval pipeline

---

## Architecture

Documents

↓

Loader

↓

Chunker

↓

Keyword Index

↓

Retriever

↓

Prompt Builder

↓

LLM

↓

Answer

---

## Learning Outcomes

- Retrieval vs. Reasoning
- Context Windows
- Document Chunking
- Prompt Augmentation
- Classical Information Retrieval
- Foundations of RAG

---

## Future Improvements

- Token-based chunking
- BM25 ranking
- Embedding search
- pgvector integration
- Hybrid retrieval

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
   - Wait for the agent to load and index local document chunks.
   - Ask questions related to the ingested documents (e.g., "who invented python").
   - The agent will search for matching context and use the local LLM to generate an answer.