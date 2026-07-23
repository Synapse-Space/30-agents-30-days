"""
Day 26
Asynchronous Document Ingestion Agent
"""

import sys
import os
import asyncio
import uuid
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from shared_core.knowledge import DocumentLoader, TextChunker
from shared_core.jobs import JobTracker
from embedder import LocalEmbedder
from database import PgVectorRepository
from pipeline import LocalKnowledgePipeline
from agent import BackgroundIngestionAgent

console = Console()

# Singleton components
_tracker = JobTracker()
_agent = None


def get_agent():
    global _agent
    if _agent is None:
        loader = DocumentLoader()
        chunker = TextChunker()
        embedder = LocalEmbedder()
        repo = PgVectorRepository("postgresql://postgres:postgres@localhost:5432/ai_agents")
        knowledge_pipeline = LocalKnowledgePipeline(loader, chunker, embedder, repo)
        _agent = BackgroundIngestionAgent(
            memory_manager=None,
            tracker=_tracker,
            knowledge_pipeline=knowledge_pipeline,
        )
    return _agent


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]Async Document Ingestion[/bold cyan]\n"
            "Day 26 • 30 AI Agents in 30 Days",
            title="Background Jobs",
        )
    )


async def async_main():
    banner()
    agent = get_agent()

    user_input = input(
        "Upload file or check status (enter file path or Job ID) > "
    ).strip()

    if not user_input:
        console.print("[yellow]No input provided.[/yellow]")
        return

    # Check if input is an existing Job ID in tracker
    existing_job = agent.get_status(user_input)
    if existing_job:
        display_job_status(existing_job)
        return

    # Otherwise treat input as file path
    filepath = user_input
    if not os.path.exists(filepath):
        console.print(f"[red]Error: File not found at '{filepath}'[/red]")
        return

    submit_res = await agent.submit(filepath)
    job_id = submit_res["job_id"]

    table = Table(title="Job Submission")
    table.add_column("Metric")
    table.add_column("Value")
    table.add_row("Job ID", job_id)
    table.add_row("File", filepath)
    table.add_row("Status", "queued")

    console.print(table)
    console.print()
    console.print(
        Panel(
            f"Upload accepted.\nBackground worker started for Job [bold cyan]{job_id}[/bold cyan].",
            title="Response",
        )
    )

    console.print("\n[bold yellow]Monitoring worker execution...[/bold yellow]")
    for _ in range(30):
        await asyncio.sleep(0.5)
        st = agent.get_status(job_id)
        if st and st["status"] in ["completed", "failed"]:
            console.print()
            display_job_status(st)
            break
        elif st and st["status"] == "processing":
            console.print(f"[cyan]Job {job_id} status: processing...[/cyan]", end="\r")


def display_job_status(job_info):
    table = Table(title=f"Worker Status: Job {job_info['id']}")
    table.add_column("Metric")
    table.add_column("Value")

    status = job_info.get("status", "unknown")
    status_str = f"[bold green]{status}[/bold green]" if status == "completed" else f"[bold yellow]{status}[/bold yellow]"
    if status == "failed":
        status_str = f"[bold red]{status}[/bold red]"

    table.add_row("Job ID", job_info["id"])
    table.add_row("Status", status_str)
    table.add_row("File", str(job_info.get("data", {}).get("file", "N/A")))

    if job_info.get("chunks") is not None:
        table.add_row("Ingested Chunks", str(job_info["chunks"]))
    if job_info.get("error"):
        table.add_row("Error", f"[red]{job_info['error']}[/red]")

    console.print(table)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()