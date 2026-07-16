
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import FormWorkflowAgent

from shared_core.workflow import CSVLoader

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

            "[bold cyan]Workflow Automation Agent[/bold cyan]\n"
            "Day 20 • 30 AI Agents in 30 Days",

            title="Workflow Engine",

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = FormWorkflowAgent(

        memory_manager=manager,

    )

    loader = CSVLoader()

    rows = loader.load(

        "sample_data.csv"

    )

    console.print(

        f"Loaded {len(rows)} workflow(s)\n"

    )

    with agent.open_authenticated_browser() as page:

        page.goto(

            "https://example.com/form",

            wait_until="networkidle",

        )

        result = agent.process(

            page,

            rows[0],

        )

    workflow = result["workflow"]

    table = Table(title="Workflow Summary")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row(

        "Status",

        workflow["status"],

    )

    table.add_row(

        "Completed Steps",

        str(workflow["completed_steps"]),

    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            result["reasoning"],

            title="AI Summary",

        )

    )


if __name__ == "__main__":

    main()