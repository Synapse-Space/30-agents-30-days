
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import LocalEmbeddingAgent

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

            "[bold cyan]Local Embedding Pipeline[/bold cyan]\n"
            "Day 24 • 30 AI Agents in 30 Days",

            title="Knowledge Ingestion",

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = LocalEmbeddingAgent(

        manager,

    )

    result = agent.ingest(

        "docs/sample.md",

    )

    table = Table(title="Knowledge Ingestion")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(

        "Chunks",

        str(result["chunks"]),

    )

    table.add_row(

        "Status",

        "Completed",

    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["summary"],

            title="AI Summary",

        )

    )


if __name__ == "__main__":

    main()