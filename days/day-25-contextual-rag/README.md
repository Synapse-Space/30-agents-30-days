# Day 25 — Anthropic-Style Contextual RAG Agent

## 📌 Overview & Objective

Day 25 implements an **Anthropic-Style Contextual RAG Agent** designed to eliminate context loss during chunking. Traditional RAG splits documents into chunks independently, causing chunks to lose global document context. Anthropic-style Contextual RAG solves this by generating concise document summaries and contextualizing chunks prior to embedding and vector storage.

---

## 🛠️ Tech Stack & Dependencies

- **Orchestration & Agent**: Custom `AnthropicStyleRAGAgent` inheriting from `ContextualRAGAgent` & `BaseAgent`
- **Vector Database**: PostgreSQL + `pgvector` extension (`psycopg` v3 driver)
- **Embedding Model**: `BAAI/bge-small-en-v1.5` (`sentence-transformers`)
- **LLM Engine**: Ollama (`llama3.1:latest`) via `langchain_ollama`
- **UI & Output**: `rich` terminal panels & tables

---

## 🏗️ Architecture & Data Flow

```text
Raw Document
     │
     ▼
Document Summarizer (Ollama llama3.1:latest)
     │
     ▼
Context-Aware Chunks (Summary + Chunk Content)
     │
     ▼
Vector Embeddings (BAAI/bge-small-en-v1.5)
     │
     ▼
PostgreSQL + pgvector Storage
     │
     ▼
Contextual Retriever (Cosine Similarity `<=>` Query Search)
     │
     ▼
Grounded Answer Generation & Explanation
```

---

## 🚀 How to Run

### 1. Prerequisites
- Ensure PostgreSQL is running locally on port 5432 with `pgvector` enabled and `ai_agents` database created.
- Ensure Ollama is running with `llama3.1:latest` pulled:
  ```bash
  ollama pull llama3.1:latest
  ```

### 2. Execution
Navigate to the day 25 directory and execute `main.py`:

```bash
cd days/day-25-contextual-rag
python3 main.py
```

### 3. Example Interaction
```text
╭─────── Semantic Retrieval ───────╮
│ Contextual RAG Agent             │
│ Day 25 • 30 AI Agents in 30 Days │
╰──────────────────────────────────╯

Question > What is Retrieval-Augmented Generation?

┌──────────────────┬──────────┐
│ Metric           │ Value    │
├──────────────────┼──────────┤
│ Retrieved Chunks │ 2        │
│ Status           │ Grounded │
└──────────────────┴──────────┘

Answer:
Retrieval-Augmented Generation (RAG) combines semantic search with large language models to retrieve relevant context before generating a response.
```

---

## 🎯 Key Learnings & Features

- **Contextual Chunking**: Prevents information loss in chunked documents.
- **pgvector Vector Operations**: Optimized Cosine Distance (`<=>`) queries with PostgreSQL.
- **Grounded LLM Generation**: Restricts model responses strictly to retrieved contextual evidence.
- **Modular Pipeline**: Clean separation between Summarizer, Retriever, Pipeline, and Agent controllers.