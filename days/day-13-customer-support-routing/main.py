"""
Day 13
Customer Support Routing Agent
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agent import CustomerSupportAgent

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

            "[bold cyan]Customer Support Routing Agent[/bold cyan]\n"
            "Day 13 • 30 AI Agents in 30 Days",

            title="Emotion-Aware AI"

        )

    )


def print_ticket(ticket):

    if ticket is None:
        return

    table = Table(title="Escalation Ticket")

    table.add_column("Field")
    table.add_column("Value")

    for key, value in ticket.items():

        table.add_row(
            str(key),
            str(value),
        )

    console.print(table)


def main():

    banner()

    postgres = PostgresClient(
        "postgresql://postgres:postgres@localhost:5432/ai_agents"
    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = CustomerSupportAgent(
        memory_manager=manager
    )

    console.print()

    console.print(
        "[green]Type 'exit' to quit.[/green]\n"
    )

    while True:

        message = input("Customer > ")

        if message.lower() == "exit":
            break

        result = agent.respond(message)

        emotion = result["emotion"]

        console.print()

        console.print(

            Panel(

                f"""
Emotion      : {emotion.emotion.value}
Score        : {emotion.score}
Confidence   : {emotion.confidence:.2f}
Keywords     : {", ".join(emotion.matched_keywords) if emotion.matched_keywords else "None"}
""",

                title="Emotion Analysis",

            )

        )

        if result["ticket"]:

            print_ticket(
                result["ticket"]
            )

        console.print(

            Panel(

                result["response"],

                title="Assistant",

            )

        )

        console.print()


if __name__ == "__main__":
    main()