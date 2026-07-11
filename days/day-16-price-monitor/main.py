
import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agent import DynamicPriceMonitorAgent

from shared_core.scraping import (
    Product,
    ProductSnapshot,
)
from shared_core.memory.postgres import PostgresClient
from shared_core.memory.repository import MemoryRepository
from shared_core.memory.manager import MemoryManager

from datetime import datetime

console = Console()


def load_snapshots(path):

    with open(path, "r", encoding="utf-8") as f:

        products = json.load(f)

    snapshots = []

    for item in products:

        product = Product(**item)

        snapshots.append(

            ProductSnapshot(

                product=product,

                timestamp=datetime.now(),

            )

        )

    return snapshots


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Dynamic Price Monitor[/bold cyan]\n"
            "Day 16 • 30 AI Agents in 30 Days",

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

    agent = DynamicPriceMonitorAgent(

        memory_manager=manager,

    )

    previous = load_snapshots(
        "sample_data/previous.json"
    )

    current = load_snapshots(
        "sample_data/current.json"
    )

    result = agent.monitor(
        previous,
        current,
    )

    table = Table(title="Price Changes")

    table.add_column("Product")
    table.add_column("Previous")
    table.add_column("Current")
    table.add_column("Status")

    for item in result["changes"]:

        table.add_row(

            item.title,

            str(item.previous),

            str(item.current),

            item.status.value,

        )

    console.print(table)

    console.print()

    console.print(

        Panel(

            "\n".join(result["alerts"]),

            title="Alerts",

        )

    )

    console.print(

        Panel(

            result["summary"],

            title="AI Summary",

        )

    )


if __name__ == "__main__":

    main()