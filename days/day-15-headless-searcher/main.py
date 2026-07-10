from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import HeadlessSearchAgent

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

            "[bold cyan]Headless Search Agent[/bold cyan]\n"
            "Day 15 • 30 AI Agents in 30 Days",

            title="Playwright + Ollama",

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = HeadlessSearchAgent(

        memory_manager=manager,

    )

    console.print()

    query = input("Search Query > ")

    result = agent.research(query)

    table = Table(title="Extracted Pages")

    table.add_column("#")
    table.add_column("Markdown Size")

    for index, document in enumerate(result["documents"], start=1):

        table.add_row(

            str(index),

            f"{len(document)} chars",

        )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["summary"],

            title="Research Summary",

        )

    )


if __name__ == "__main__":

    main()