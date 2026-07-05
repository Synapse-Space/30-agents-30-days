"""
Day 10 - Multi Session Memory Chatbot
"""

from rich.console import Console
from rich.panel import Panel

from agent import MemoryChatbot

from shared_core.memory.postgres import (
    PostgresClient,
)

from shared_core.memory.repository import (
    MemoryRepository,
)

from shared_core.memory.manager import (
    MemoryManager,
)

from shared_core.llm_client import LLMClient

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Multi-Session Memory Chatbot[/bold cyan]\n"
            "Day 10 • 30 AI Agents in 30 Days",

            title="Persistent Memory"

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    llm = LLMClient()

    chatbot = MemoryChatbot(

        manager,

        llm,

    )

    user_id = input("User ID > ")

    console.print()

    console.print(

        "[green]Type 'exit' to quit.[/green]\n"

    )

    while True:

        message = input("You > ")

        if message.lower() == "exit":

            break

        response = chatbot.chat(

            user_id=user_id,

            message=message,

        )

        console.print()

        console.print(

            Panel(

                response,

                title="Assistant",

            )

        )

        console.print()


if __name__ == "__main__":

    main()