from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from langchain_ollama import ChatOllama
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import ReflectionGraphAgent

from shared_core.memory.postgres import (
    PostgresClient,
)

from shared_core.memory.repository import (
    MemoryRepository,
)

from shared_core.memory.manager import (
    MemoryManager,
)

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Reflective Reasoning Agent[/bold cyan]\n"
            "Day 22 • 30 AI Agents in 30 Days",

            title="LangGraph",

        )

    )


def main():

    banner()

    llm = ChatOllama(

        model="llama3.1:latest"

    )

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = ReflectionGraphAgent(

        llm,

        manager,

    )

    prompt = input(

        "Prompt > "

    )

    result = agent.reflect(

        prompt,

    )

    table = Table(title="Reflection Summary")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(

        "Iterations",

        str(result["iterations"]),

    )

    table.add_row(

        "Final Score",

        str(result["score"]),

    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["answer"],

            title="Final Answer",

        )

    )

    console.print()

    console.print(

        Panel(

            result["reasoning"],

            title="AI Reflection",

        )

    )


if __name__ == "__main__":

    main()