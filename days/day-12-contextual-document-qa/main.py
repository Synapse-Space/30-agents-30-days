from rich.console import Console
from rich.panel import Panel

from agent import ContextualDocumentAgent

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

            "[bold cyan]Contextual Document Q&A Agent[/bold cyan]\n"
            "Day 12 • 30 AI Agents in 30 Days",

            title="Knowledge Retrieval",

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = ContextualDocumentAgent(

        memory_manager=manager,

    )

    chunks = agent.load_documents(

        "sample_docs"

    )

    console.print(

        f"[green]Loaded {chunks} document chunks.[/green]\n"

    )

    console.print(

        "[yellow]Ask questions about the documents.[/yellow]"

    )

    console.print(

        "[green]Type 'exit' to quit.[/green]\n"

    )

    while True:

        question = input("You > ")

        if question.lower() == "exit":

            break

        result = agent.ask(question)

        console.print()

        console.print(

            Panel(

                result["response"],

                title="Answer",

            )

        )

        console.print(

            Panel(

                result["context"],

                title="Retrieved Context",

            )

        )

        console.print()


if __name__ == "__main__":

    main()