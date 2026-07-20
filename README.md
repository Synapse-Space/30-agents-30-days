# 30-Agents-30-Days: Systems-First Agentic Engineering

> "AI can generate, refactor, and explain code. But AI cannot replace your understanding of system design, architectural trade-offs, problem decomposition, and product thinking."

Welcome to **30-Agents-30-Days**—a public engineering marathon focused on building production-grade autonomous AI agents from scratch. This repository is not a collection of toy scripts or prompt-engineered loops; it is a progressive exploration of distributed systems, state machines, and resilient architectures built to handle real-world operational challenges.

## 🔬 The Thesis

Too many developers are learning how to prompt models without learning how software systems actually work. When LLMs leave sandboxed environments and hit real production data, simple prompt wrappers break. 

This journey is a commitment to keeping humans responsible for the **thinking, structuring, and engineering decisions**. Over 30 days, the architecture transitions from simple single-file ReAct loops to enterprise-grade asynchronous microservices utilizing robust state orchestration tools.

---

## 🛠️ The Tech Stack (100% Open-Source & Production-Ready)

To ensure maximum scalability without vendor lock-in or fragile API dependencies, this ecosystem prioritizes rugged, open-source infrastructure:
*   **Orchestration & State:** LangGraph & Rasa Open Source (for deterministic, non-hallucinating state machines).
*   **Asynchronous Queuing:** `pg-boss` (PostgreSQL-backed job queue for decoupling heavy AI processing).
*   **Vector Infrastructure:** PostgreSQL + `pgvector` (for enterprise-scale, high-performance RAG pipelines).
*   **Browser Automation:** Playwright (for building autonomous, multi-modal web-browsing execution agents).
*   **Local & Edge Models:** Ollama (Llama 3), HuggingFace Sentence Transformers (`bge-small-en-v1.5`), and Groq Free Tier.

---

## 📅 The 30-Day Architecture Matrix

| Day | Project Name | Core Patterns & Frameworks | System Design Focus |
| :--- | :--- | :--- | :--- |
| **Week 1** | **Foundation & Tool Use** | | |
| 01 | [Basic Calculator Agent](./days/day-01-reAct-calculator) | Native Python, ReAct Loop | Stateful Reason-Act-Observe Execution |
| 02 | [Weather-Buster Assistant](./days/day-02-weather-buster) | OpenAI Tool Calling, REST APIs | JSON Schema Binding & Functional Boundaries |
| 03 | [Structured Data Extractor](./days/day-03-structured-data-extractor) | Pydantic, Structured Outputs | Formatting Enforcement & Validation Layers |
| 04 | [Intelligent SQL Query Builder](./days/day-04-sql-query-builder) | DB Schema Reflection, Prompt Guardrails | Context Injection & Secure Execution |
| 05 | [Smart Email Responder](./days/day-05-smart-email-responder) | Intent Classification, Dynamic Templates | Routing Logic & Contextual Hydration |
| 06 | [CLI File-System Commander](./days/day-06-cli-filesystem-commander) | Deterministic File OS Modules | Safety Pre-flight Checklists & Risk Mitigation |
| 07 | [Market Watcher Alert Engine](./days/day-07-fx-sentinel) | Cron Scheduling, State Persistence | Long-polling vs Event-driven Triggers |
| **Week 2** | **Memory & Multi-Turn State** | | |
| 08 | [Conversational Reminder Bot](./days/day-08-conversational-reminder-bot) | Short-term Memory Context | Entity Extraction & Temporal Parsing |
| 09 | [User Onboarding State-Machine](./days/day-09-user-profile-onboarding) | Linear Dialogues, Strict Boundaries | Context Lockouts & Multi-turn Validation |
| 10 | [Multi-Session Memory Chatbot](./days/day-10-multi-session-memory-chatbot) | PostgreSQL Database Drivers | Long-term Memory Hydration & Session Keys |
| 11 | [Deterministic FAQ Guardrail](./days/day-11-deterministic-faq-guardrail) | RapidFuzz, Rule-Based Routing | Merging Rule-based Intents with LLM Fallbacks |
| 12 | [Contextual Document Q&A](./days/day-12-contextual-document-qa) | Native Text Chunking, In-memory Search | Word Windowing & Overlap Trade-offs |
| 13 | [Customer Support Router](./days/day-13-customer-support-routing) | Sentiment Analysis, Escalation Triggers | Conditional Routing & Dynamic System Prompts |
| 14 | [Automated Code Reviewer](./days/day-14-code-review-assistant) | Abstract Syntax Trees (AST), Local Models | Code Structural Analysis & Static Guardrails |
| **Week 3** | **Autonomous Web & Browser Agents** | | |
| 15 | [Headless Searcher](./days/day-15-headless-searcher) | Playwright, Wikipedia Search Scraping | Web Scraping & Markdown Compilation |
| 16 | [E-Commerce Price Monitor](./days/day-16-price-monitor) | Pydantic Schemas, Change Detection | Structured Data Analysis & Alerting Rules |
| 17 | [Authenticated Profile Analyzer](./days/day-17-authenticated-profile-analyzer) | Auth-Aware Automated Browser | Secure Cookie Storage & Session Resiliency |
| 18 | [Visual UI Agent](./days/day-18-visual-ui-agent) | Ollama Vision (Qwen3-VL) | Translating Screenshots to Absolute DOM Coordinates |
| 19 | [Selector-Free Browser Agent](./days/day-19-selector-free-agent) | Vision Feedback Loops, Ollama (Qwen3-VL) | Autonomously Recovering from Broken CSS Selectors |
| 20 | [Workflow Automation Agent](./days/day-20-workflow-automation) | CSV Streaming Pipelines | Batch Ingestion & Dynamic Error Exception Handling |
| 21 | [Content Delivery Agent](./days/day-21-content-delivery) | Content Management System (CMS) APIs | Draft Syncing, Validation, and State Reporting |
| **Week 4** | **Enterprise Orchestration & Asynchronous Scaling** | | |
| 22 | [Reflective Reasoning Agent](./days/day-22-reflective-reasoning) | LangGraph, Iterative Nodes | Writer-Critic Node Synchronization |
| 23 | [Parallel Research Agent](./days/day-23-parallel-research) | Supervisor Design Pattern, Concurrency | Multi-threaded Fan-out & Report Compilations |
| 24 | [Local Embedding Pipeline](./days/day-24-local-embedding) | HuggingFace, PostgreSQL + `pgvector` | Vector Clustering, Dimensionality, Index Optimization |
| 25 | [Contextual RAG Engine](./days/day-25-contextual-rag) | Global Text Chunk Summarizations | Minimizing Information Loss in Heavy Enterprise Docs |
| 26 | [Asynchronous Ingestion Worker](./days/day-26-pgboss-ingestion) | `pg-boss` Job Queuing, FastAPIs | Decoupling HTTP Requests from Heavy AI Pipelines |
| 27 | [Self-Healing Error Recovery Worker](./days/day-27-self-healing-worker) | State Loop Backtracking, Queue Retries | Runtime Stack-Trace Evaluation & Code Rewriting |
| 28 | [Dual-Core Dialogue Hybrid](./days/day-28-dual-core-hybrid) | Rasa Engine + LangGraph Routing | Deterministic Intent Boundary Management |
| 29 | [Distributed Log-Analysis Monitor](./days/day-29-log-monitor) | Streaming WebSockets, Security Filtering | Real-time Anomaly Vectors over Streaming Logs |
| 30 | [The Autonomous Solution Architect](./days/day-30-solution-architect) | Full Integration Architecture | Microservice Orchestration & End-to-End Synergy |

---

## 🏗️ Repository Blueprint

The repository is built as an organized monorepo, ensuring core architectural boilerplate isn't rewritten unnecessarily:

```text
30-agents-30days/
├── shared_core/                  # Centralized infrastructure utilities
│   ├── database.py               # Singleton connections for pgvector/pg-boss
│   ├── llm_client.py             # Optimized LLM inference clients & fallback configs
│   └── logger.py                 # Structured production logging for trace debugging
├── days/                         # Day-by-day isolated system environments
│   ├── day-01-react-calculator/
│   │   ├── agent.py
│   │   └── README.md             # Architecture diagram & lessons learned
│   └── day-26-pgboss-ingestion/  
│       ├── docker-compose.yml    # Spin up local Postgres infrastructure
│       ├── api_server/           # Web entry point
│       └── worker_node/          # Asynchronous job consumers
└── README.md                     # Master Directory
```

🚀 Getting Started Locally

1. Clone and Initialize Environment
```bash
git clone https://github.com/YOUR_USERNAME/30-agents-30days.git
cd 30-agents-30days
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

2. Set Up Environment Variables
Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```
Fill in your local connection parameters and necessary free-tier API parameters (such as Groq keys or local Ollama endpoints).

3. Spin up Shared Infrastructure
For projects requiring advanced persistence or message brokers (Weeks 3 & 4), spin up the Docker ecosystem:
```bash
docker-compose up -d
```

📈 Building in Public & Contact
I am actively documenting the exact failures, architectural friction, and edge cases discovered during this sprint across socials.

Follow the Journey: #BuildInPublic

LinkedIn: [Your Profile Link Here]
Email: [Your Professional Email Here]

***

### 💡 Pro Tip for GitHub:
When you push this code to GitHub, leave the daily folders unlinked at first. As you finish a day's project, convert that day's entry in the markdown table into a live clickable hyperlink (e.g., replace `Basic Calculator Agent` with `[Basic Calculator Agent](./days/day-01-react-calculator)`). This keeps your portfolio clean and shows real-time progress to tracking recruiters!