# Day 23 — Parallel Research Agent

## Objective

Build a LangGraph-based multi-agent research system where a supervisor distributes work to parallel research agents and combines their findings into a single executive report.

---

## Features

- Supervisor node
- Parallel research workers
- Shared team state
- Result aggregation
- Executive report generation
- LangGraph orchestration

---

## Architecture

Query
↓
Supervisor
↓
Parallel Researchers (Market, Tech, Trends)
↓
Aggregator
↓
Executive Report

---

## Learning Outcomes

- Parallel graph execution
- Fan-out / Fan-in workflows
- Multi-agent coordination
- Shared state management
- Result aggregation
- Collaborative AI systems

---

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Agent:**
   ```bash
   python main.py
   ```

3. **Execution Flow:**
   - Input a research topic when prompted (e.g., `Research Topic > Quantum Computing`).
   - The graph executes in parallel, fanning out the query to three different specialized researchers: `MarketResearcher`, `TechnologyResearcher`, and `TrendsResearcher`.
   - The state is merged concurrently using `typing.Annotated` and `operator.add` to track the number of completed workers.
   - An `ExecutiveReportGenerator` receives the compiled research and generates a final unified report.
   - A summary of the execution is printed alongside the final executive report.

---

## Future Improvements

- Dynamic worker allocation
- Web search integration
- Source verification
- Research confidence scoring
- Human review
- Distributed execution