
import asyncio

from rich.console import Console
from rich.panel import Panel

from agent import EnterpriseArchitect

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Fully Autonomous Solution Architect[/bold cyan]\n"
            "Day 30 • 30 AI Agents in 30 Days",

            title="Grand Finale",

        )

    )


async def main():

    banner()

    architect = EnterpriseArchitect(
        memory_manager=None
    )

    objective = input(
        "\nObjective > "
    )

    results = await architect.solve(
        objective
    )

    console.print()

    console.print(
        Panel(
            str(results),
            title="Workflow Result",
        )
    )


if __name__ == "__main__":

    asyncio.run(main())