# Day 25 — Anthropic-Style Contextual RAG Agent

## Objective

Build a Retrieval-Augmented Generation (RAG) pipeline that improves retrieval quality by summarizing each document first and prepending that summary to every chunk before embedding.

---

## Features

- Document summarization
- Context-aware chunk generation
- Local embeddings
- pgvector semantic retrieval
- Grounded answer generation
- Modular RAG architecture

---

## Architecture

Document

↓

Summary

↓

Contextual Chunks

↓

Embeddings

↓

pgvector

↓

Semantic Retrieval

↓

Grounded LLM Answer

---

## Learning Outcomes

- Contextual Retrieval
- RAG architecture
- Semantic search
- Query embeddings
- Grounded AI responses
- Vector databases

---

## Future Improvements

- Hybrid BM25 + Vector Search
- Cross-encoder reranking
- Streaming responses
- Multi-document retrieval
- Citation support
- Source confidence scoring