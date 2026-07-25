

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agent import EnterpriseAssistant

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Dual-Core Dialogue Hybrid[/bold cyan]\n"
            "Day 28 • 30 AI Agents in 30 Days",

            title="Hybrid Conversation",

        )

    )


def main():

    banner()

    assistant = EnterpriseAssistant(
        memory_manager=None
    )

    while True:

        message = input(
            "\nYou > "
        )

        if message.lower() in (
            "exit",
            "quit",
        ):
            break

        result = assistant.chat(
            message
        )

        table = Table(title="Routing")

        table.add_column("Property")
        table.add_column("Value")

        table.add_row(
            "Engine",
            result.engine.value,
        )

        console.print(table)

        console.print()

        console.print(

            Panel(

                result.response,

                title="Assistant",

            )

        )


if __name__ == "__main__":
    main()