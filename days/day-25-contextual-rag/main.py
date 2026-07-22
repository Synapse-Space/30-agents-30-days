
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agent import AnthropicStyleRAGAgent

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

            "[bold cyan]Contextual RAG Agent[/bold cyan]\n"
            "Day 25 • 30 AI Agents in 30 Days",

            title="Semantic Retrieval",

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = AnthropicStyleRAGAgent(

        manager,

    )

    question = input(

        "Question > "

    )

    result = agent.ask(

        question,

    )

    table = Table(title="Retrieval Summary")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(

        "Retrieved Chunks",

        str(result["sources"]),

    )

    table.add_row(

        "Status",

        "Grounded",

    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["answer"],

            title="Answer",

        )

    )

    console.print()

    console.print(

        Panel(

            result["reasoning"],

            title="Retrieval Explanation",

        )

    )


if __name__ == "__main__":

    main()