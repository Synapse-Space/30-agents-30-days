# Day 02 — Weather-Buster Assistant

## Goal

Understand how to bind LLMs to deterministic Python functions using Native Tool Calling (JSON Schemas) and integrate with external REST APIs.

---

## Concepts

- Native Tool Calling / Function Calling
- JSON Schema Binding
- External API Integration
- Tool Registries (Functional Boundaries)
- Asynchronous Tool Execution

---

## Architecture

(User)

↓

(LLM) — *Prompted with JSON Schema Tool Definitions*

↓

(Tool Call Requested) — *Returns Structured JSON `tool_calls`*

↓

(Tool Registry) — *Maps string name to Python function*

↓

(Weather API) — *Makes HTTP request to Open-Meteo*

↓

(Observation) — *JSON payload sent back to LLM context*

↓

(Final Answer) — *Natural Language response generated*

---

## Folder Structure

```
day-02-weather-buster/
├── agent.py         # The WeatherAgent that orchestrates the tool-calling loop
├── main.py          # Interactive terminal entry point
├── tool_schema.py   # JSON Schema definition of the `get_weather` tool for the LLM
└── weather_api.py   # The actual Python implementation that makes HTTP requests to Open-Meteo
```
*Note: This day introduces `shared_core/tools/registry.py` which manages the mapping between the LLM's requested tool names and our actual Python functions.*

---

## Code Walkthrough

- **`main.py`**: Initializes the agent and runs an interactive `while True` loop to take user queries and print the agent's responses.
- **`agent.py`**: Instead of manually parsing text using Regex (like Day 1), this agent uses the LLM's native `.chat()` interface and passes in a list of `tools`. If the LLM returns `tool_calls`, the agent dynamically fetches the target function from the `ToolRegistry`, executes it with the provided arguments, and appends the result as a `tool` role message back into the conversation history.
- **`tool_schema.py`**: Defines the `WEATHER_TOOL` using standard JSON Schema syntax. This acts as the "contract" between the LLM and our Python code, strictly defining what the `get_weather` function does and that it requires a `city` string.
- **`weather_api.py`**: A dedicated API client that hits the Open-Meteo geocoding API to convert a city name into latitude/longitude, and then hits the forecast API to get the current temperature, humidity, and wind speed.
- **`shared_core/tools/registry.py`**: A dictionary-backed class that registers string tool names (e.g. `"get_weather"`) to actual Python callables (`WeatherAPI.get_weather`), allowing safe and dynamic execution of functions that the LLM requests.

---

## Lessons Learned

- **Native Tool Calling**: Modern LLMs are explicitly fine-tuned to return structured JSON `tool_calls`. This is vastly superior and less fragile than prompting the model to format raw text that we have to parse via Regex.
- **JSON Schemas as Contracts**: The LLM relies completely on the descriptions and parameter types defined in the JSON Schema. If the schema is vague, the LLM will hallucinate arguments.
- **Separation of Concerns**: Moving the tool execution out of the agent and into a `ToolRegistry` allows the agent to be completely agnostic to *what* tools it has access to, making the system incredibly scalable.

---

## Challenge

Modify the `weather_api.py` and `tool_schema.py` to support a new tool: **`get_forecast`** which returns the expected weather for the next 7 days instead of just the current weather!

---

## Next Day Preview

Tomorrow we build a Structured Data Extractor using Pydantic to strictly enforce formatting constraints.
