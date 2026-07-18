# Day 22 — Reflective Reasoning Agent

## Objective

Build a LangGraph-powered AI agent that iteratively improves its responses using a Writer–Critic reflection loop until a quality threshold is reached.

---

## Features

- LangGraph workflow
- Shared graph state
- Writer node
- Critic node
- Conditional routing
- Reflection loop
- AI-generated execution summary

---

## Architecture

Prompt
↓
Writer
↓
Critic
↓
Controller
↓
Retry / Finish

---

## Learning Outcomes

- LangGraph fundamentals
- Stateful execution
- Conditional graph edges
- Reflection-based reasoning
- Adaptive AI workflows
- Graph orchestration

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
   - Input a prompt when prompted (e.g., `Prompt > Tell me about the OKF vector database`).
   - The graph delegates the prompt to the `WriterNode`.
   - The output is passed to the `CriticNode` where a secondary LLM evaluates the answer and gives it a structured score and feedback.
   - The `ReflectionController` decides if the graph is finished (score > threshold or max iterations reached) or if it needs to loop back to the `WriterNode` to try again based on the feedback.
   - A final summary of the execution iterations and reflection logic is printed.

---

## Future Improvements

- Planner node
- Tool-calling node
- Human approval node
- Multi-agent collaboration
- Parallel graph execution
- Memory-aware reasoning