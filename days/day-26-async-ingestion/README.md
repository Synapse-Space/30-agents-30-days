# Day 26 — Asynchronous Document Ingestion Agent

## 📌 Overview & Objective

Day 26 implements an **Asynchronous Document Ingestion Engine** that decouples long-running AI document processing (PDF parsing, text chunking, and vector embedding generation) from HTTP/CLI client interactions.

When a file is submitted, the system returns an immediate **Job ID** with status `queued` while a background worker processes the document asynchronously and saves vector embeddings into PostgreSQL (`pgvector`).

---

## 🛠️ Tech Stack & Dependencies

- **Job Queue & Tracker**: `AsyncJobQueue` and `JobTracker` for background task dispatch and lifecycle state management
- **Worker Execution**: `IngestionWorker` running non-blocking background tasks
- **Document Parser**: `pypdf` (PDF support) & UTF-8 text loader
- **Vector Embeddings**: `BAAI/bge-small-en-v1.5` (`sentence-transformers`)
- **Database Storage**: PostgreSQL + `pgvector` extension via `psycopg` v3
- **CLI Interface**: `rich` formatted panels, tables, and real-time status updates

---

## 🏗️ Architecture & Data Flow

```text
Client / CLI / API Endpoint
             │
             ▼
  Submit Document Path / Upload
             │
             ├────────────────────────────────────────┐
             ▼                                        ▼
   Immediate Job ID Returned               Async Job Queue (job_queue.py)
      (Status: "queued")                              │
                                                      ▼
                                           Ingestion Worker (worker.py)
                                                      │
                                                      ├─► Update Status: "processing"
                                                      ├─► Extract PDF/Text Content (pypdf)
                                                      ├─► Chunk Text (500 chars)
                                                      ├─► Compute BGE Embeddings
                                                      ├─► Save to PostgreSQL (document_chunks)
                                                      └─► Update Status: "completed"
```

---

## 🚀 How to Run

### 1. Prerequisites
- Ensure PostgreSQL is running on `localhost:5432` with the `ai_agents` database and `pgvector` extension enabled.
- Virtual environment with required dependencies:
  ```bash
  source venv/bin/activate
  ```

### 2. Launch Ingestion CLI
Navigate to the Day 26 directory and start the engine:

```bash
cd days/day-26-async-ingestion
python3 main.py
```

### 3. File Submission & Real-Time Tracking
Input a local file path (e.g., PDF or Markdown document):

```text
Upload file or check status (enter file path or Job ID) > /home/13843K/Downloads/Yuvraj Singh - SDE1.pdf
```

**Output**:
```text
Job Submission
┌──────────┬─────────────────────────────────────────────────┐
│ Metric   │ Value                                           │
├──────────┼─────────────────────────────────────────────────┤
│ Job ID   │ 6dba7e6b                                        │
│ File     │ /home/13843K/Downloads/Yuvraj Singh - SDE1.pdf │
│ Status   │ queued                                          │
└──────────┴─────────────────────────────────────────────────┘

Monitoring worker execution...

Worker Status: Job 6dba7e6b
┌────────────────┬─────────────────────────────────────────────────┐
│ Metric         │ Value                                           │
├────────────────┼─────────────────────────────────────────────────┤
│ Job ID         │ 6dba7e6b                                        │
│ Status         │ completed                                       │
│ File           │ /home/13843K/Downloads/Yuvraj Singh - SDE1.pdf │
│ Ingested Chunks│ 8                                               │
└────────────────┴─────────────────────────────────────────────────┘
```

### 4. Query Existing Job Status
Check the status of any previously submitted job anytime by supplying its **Job ID**:

```text
Upload file or check status (enter file path or Job ID) > 6dba7e6b
```

---

## 🎯 Key Learnings & Features

- **Asynchronous Task Offloading**: Prevents client request timeouts by returning immediate job acknowledgements.
- **Full Job Lifecycle Tracking**: Complete visibility into state transitions (`queued` ➔ `processing` ➔ `completed` / `failed`).
- **Multi-Format Document Parsing**: Support for `.pdf`, `.md`, and `.txt` files out of the box.
- **Production AI Infrastructure**: Decoupled, modular worker-queue design suitable for background worker scale-out.