"""
Day 11
Deterministic FAQ Guardrail Agent
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rich.console import Console
from rich.panel import Panel

from agent import FAQGuardrailAgent

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

            "[bold cyan]FAQ Guardrail Agent[/bold cyan]\n"
            "Day 11 • 30 AI Agents in 30 Days",

            title="Hybrid AI",

        )

    )


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = FAQGuardrailAgent(

        memory_manager=manager,

    )

    console.print()

    console.print(

        "[green]Type 'exit' to quit[/green]\n"

    )

    while True:

        user = input("You > ")

        if user.lower() == "exit":

            break

        result = agent.chat(user)

        console.print()

        console.print(

            Panel(

                result["response"],

                title=result["source"],

            )

        )

        console.print()


if __name__ == "__main__":

    main()