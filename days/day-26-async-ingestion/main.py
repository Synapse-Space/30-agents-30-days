"""
Day 26
Asynchronous Document Ingestion Agent
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import uuid

console = Console()


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]Async Document Ingestion[/bold cyan]\n"
            "Day 26 • 30 AI Agents in 30 Days",
            title="Background Jobs",
        )
    )


def submit_job(filename: str):
    job_id = str(uuid.uuid4())[:8]

    return {
        "job_id": job_id,
        "status": "queued",
    }


def main():

    banner()

    filename = input(
        "Upload file > "
    )

    result = submit_job(
        filename
    )

    table = Table(title="Job Status")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "Job ID",
        result["job_id"],
    )

    table.add_row(
        "Status",
        result["status"],
    )

    console.print(table)

    console.print()

    console.print(
        Panel(
            "The upload has been accepted.\n"
            "Background workers will process the document "
            "and generate embeddings asynchronously.",
            title="Response",
        )
    )


if __name__ == "__main__":
    main()