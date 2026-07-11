
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import ProfileAnalyzerAgent

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

            "[bold cyan]Authenticated Profile Analyzer[/bold cyan]\n"
            "Day 17 • 30 AI Agents in 30 Days",

            title="Playwright + Ollama",

        )

    )


def print_profile(profile):

    table = Table(title="Profile Statistics")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row(
        "Name",
        profile.summary.name,
    )

    table.add_row(
        "Headline",
        profile.summary.headline,
    )

    table.add_row(
        "Location",
        profile.summary.location,
    )

    table.add_row(
        "Followers",
        str(profile.statistics.followers),
    )

    table.add_row(
        "Connections",
        str(profile.statistics.connections),
    )

    table.add_row(
        "Posts",
        str(profile.statistics.posts),
    )

    console.print(table)


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = ProfileAnalyzerAgent(

        memory_manager=manager,

    )

    profile_url = input(
        "Profile URL > "
    )

    result = agent.analyze_profile(
        profile_url
    )

    print_profile(
        result["profile"]
    )

    console.print()

    console.print(

        Panel(

            "\n".join(
                result["metrics"]
            ),

            title="Detected Insights",

        )

    )

    console.print(

        Panel(

            result["summary"],

            title="AI Analysis",

        )

    )


if __name__ == "__main__":

    main()