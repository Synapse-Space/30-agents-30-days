"""
Day 14
Code Review Assistant
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agent import PythonCodeReviewAgent

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

            "[bold cyan]Code Review Assistant[/bold cyan]\n"
            "Day 14 • 30 AI Agents in 30 Days",

            title="AST + AI",

        )

    )


def print_findings(report):

    table = Table(title="Static Analysis")

    table.add_column("Rule")
    table.add_column("Severity")
    table.add_column("Line")
    table.add_column("Message")

    for finding in report.findings:

        table.add_row(

            finding.rule,

            finding.severity.value,

            str(finding.line),

            finding.message,

        )

    console.print(table)


def main():

    banner()

    postgres = PostgresClient(

        "postgresql://postgres:postgres@localhost:5432/ai_agents"

    )

    repository = MemoryRepository(postgres)

    manager = MemoryManager(repository)

    agent = PythonCodeReviewAgent(

        memory_manager=manager,

    )

    console.print()

    file_path = input(

        "Python file to review: "

    )

    result = agent.review(file_path)

    console.print()

    print_findings(

        result["report"]

    )

    console.print()

    console.print(

        Panel(

            f"Overall Score: {result['report'].score}/100",

            title="Quality Score",

        )

    )

    console.print(

        Panel(

            result["review"],

            title="AI Review",

        )

    )


if __name__ == "__main__":

    main()