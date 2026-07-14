
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import VisualInteractionAgent

from shared_core.memory.postgres import PostgresClient
from shared_core.memory.repository import MemoryRepository
from shared_core.memory.manager import MemoryManager

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Selector-Free Browser Agent[/bold cyan]\n"
            "Day 19 • 30 AI Agents in 30 Days",

            title="Vision + Playwright",

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = VisualInteractionAgent(

        memory_manager=manager,

    )

    url = input("URL > ")

    instruction = input(

        "Instruction > "

    )

    with agent.open_authenticated_browser() as page:

        page.goto(

            url,

            wait_until="networkidle",

        )

        result = agent.interact(

            page,

            instruction,

        )

    if not result["target"]:
        console.print(Panel(result["reasoning"], title="AI Reasoning"))
        return

    target = result["target"]["element"]

    coords = result["target"]["coordinates"]

    table = Table(title="Interaction Result")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Target", target.label)

    table.add_row(
        "Type",
        target.element_type.value,
    )

    table.add_row(
        "Confidence",
        f"{target.confidence:.2f}",
    )

    table.add_row(
        "Coordinates",
        str(coords),
    )

    table.add_row(
        "Verified",
        str(result["success"]),
    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["reasoning"],

            title="AI Reasoning",

        )

    )


if __name__ == "__main__":

    main()