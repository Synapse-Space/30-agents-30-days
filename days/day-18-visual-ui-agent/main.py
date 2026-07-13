
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import VisualUIAgent

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

            "[bold cyan]Visual UI Agent[/bold cyan]\n"
            "Day 18 • 30 AI Agents in 30 Days",

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

    agent = VisualUIAgent(

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

        result = agent.locate(

            page,

            instruction,

        )

    target = result["target"]["element"]

    coords = result["target"]["coordinates"]

    table = Table(title="Detected Target")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row(

        "Label",

        target.label,

    )

    table.add_row(

        "Type",

        target.element_type.value,

    )

    table.add_row(

        "Confidence",

        f"{target.confidence:.2f}",

    )

    table.add_row(

        "Bounding Box",

        str(target.bounding_box),

    )

    table.add_row(

        "Center",

        str(coords),

    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["reasoning"],

            title="AI Explanation",

        )

    )


if __name__ == "__main__":

    main()