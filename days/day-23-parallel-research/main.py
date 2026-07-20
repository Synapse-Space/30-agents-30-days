
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from langchain_ollama import ChatOllama

from agent import ParallelResearchGraphAgent

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

            "[bold cyan]Parallel Research Agent[/bold cyan]\n"
            "Day 23 • 30 AI Agents in 30 Days",

            title="LangGraph Supervisor",

        )

    )


def main():

    banner()

    llm = ChatOllama(

        model="llama3.1:8b"

    )

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = ParallelResearchGraphAgent(

        llm,

        manager,

    )

    topic = input(

        "Research Topic > "

    )

    result = agent.research(

        topic,

    )

    table = Table(title="Research Summary")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(

        "Workers",

        str(result["workers"]),

    )

    table.add_row(

        "Status",

        result["status"],

    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["report"],

            title="Executive Report",

        )

    )


if __name__ == "__main__":

    main()