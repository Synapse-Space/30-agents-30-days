# Day 24 — Local Embedding Pipeline

## Objective

Build a local document ingestion pipeline that generates embeddings using Hugging Face models and stores them in a pgvector-enabled PostgreSQL database.

---

## Features

- Local embedding generation
- Document chunking
- pgvector storage
- Metadata persistence
- Modular ingestion pipeline
- AI-generated ingestion summary

---

## Architecture

Documents

↓

Loader

↓

Chunker

↓

Embedding Model

↓

Vector Store

↓

Knowledge Base

---

## Learning Outcomes

- Sentence Transformers
- Vector embeddings
- pgvector
- Semantic search foundations
- Document preprocessing
- Knowledge ingestion pipelines

---

## Future Improvements

- PDF ingestion
- DOCX support
- Recursive chunking
- Batch processing
- Hybrid search
- Incremental indexing