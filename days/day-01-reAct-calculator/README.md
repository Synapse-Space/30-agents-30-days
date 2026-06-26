# Day 01 — ReAct Calculator Agent

## Goal

Understand how an AI Agent works internally.

---

## Concepts

- ReAct
- Thought
- Action
- Observation
- Tool Calling

---

## Architecture

(User)

↓

(LLM)

↓

(Reason)

↓

(Action)

↓

(Calculator)

↓

(Observation)

↓

(Final Answer)

---

## Folder Structure

```
day-01-reAct-calculator/
├── agent.py     # Contains the ReActAgent that controls the LLM execution loop
├── main.py      # Entry point for the REPL interface to talk to the agent
├── parser.py    # Regex-based parser to extract thoughts, actions, and answers
└── tools.py     # Tool implementations, specifically the calculator function
```

---

## Code Walkthrough

- **`main.py`**: Initializes the agent and provides a continuous interactive terminal loop (`while True`). It takes user input and passes it to the `agent.run(query)` function.
- **`agent.py`**: Contains the core logic of the ReAct pattern. Inside `agent.run()`, a `max_iterations` loop is defined. The agent sends the full conversation history to the LLM, parses the response, and if an action is requested, executes the chosen tool. The tool's output is appended back as an "Observation" and the loop continues until a "Final Answer" is reached.
- **`parser.py`**: Provides the `ReActParser` class with compiled Regular Expressions. It extracts `Thought:`, `Action:`, `Action Input:`, and `Final Answer:` blocks from the LLM's raw text response and structures them cleanly into an `AgentResponse` dataclass.
- **`tools.py`**: Implements the actual tools the agent can use. The `calculator` function safely evaluates mathematical expressions using Python's `eval()` function inside a restricted environment that limits the available built-in functions to a whitelist.

---

## Lessons Learned

- **Prompt Engineering**: The success of the agent depends heavily on the `SYSTEM_PROMPT` instructing it exactly how to format its thoughts and actions.
- **Output Parsing**: Text-based LLMs need robust parsers (like Regex) to translate open-ended text into actionable software commands.
- **Tool Routing**: Mapping the string output of the LLM (e.g., `"calculator"`) to an actual Python function reference allows the agent to affect the real world and perform tasks it can't natively do (like exact math).
- **The Observation Loop**: By feeding the results of tools back into the chat history, the LLM can "observe" the outcome and reason about the next step until the task is complete.

---

## Challenge

Modify the calculator to support:

- sqrt
- %
- exponentiation

---

## Next Day Preview

Tomorrow we build a Multi-Tool Agent.
