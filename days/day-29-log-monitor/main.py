
import asyncio

from rich.console import Console
from rich.panel import Panel

from agent import EnterpriseMonitoringAgent

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Distributed Log Monitor[/bold cyan]\n"
            "Day 29 • 30 AI Agents in 30 Days",

            title="Live Monitoring",

        )

    )


async def main():

    banner()

    agent = EnterpriseMonitoringAgent(

        websocket_url="ws://localhost:8000/logs",

        memory_manager=None,

    )

    console.print()

    console.print(

        "[green]Monitoring started...[/green]"

    )

    console.print()

    await agent.start()


if __name__ == "__main__":

    asyncio.run(main())