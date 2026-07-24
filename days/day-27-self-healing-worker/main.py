
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agent import RecoveryAgent

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Self-Healing Worker[/bold cyan]\n"
            "Day 27 • 30 AI Agents in 30 Days",

            title="Recovery Pipeline",

        )

    )


def main():

    banner()

    payload = {

        "file": "sample.pdf"

    }

    agent = RecoveryAgent()

    result = agent.submit(payload)

    table = Table(title="Task Submitted")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "Task ID",
        result["task_id"],
    )

    table.add_row(
        "Status",
        result["status"],
    )

    console.print(table)

    console.print()

    console.print(

        Panel(

            "If the task fails, the worker will analyze "
            "the exception, ask the LLM for a repair, "
            "and retry automatically.",

            title="Execution Flow",

        )

    )


if __name__ == "__main__":
    main()