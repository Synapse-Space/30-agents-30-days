from pathlib import Path 
from rich.console import Console 
from rich.panel import Panel 
from rich.table import Table 

from agent import CMSPublishingAgent

from shared_core.publishing import ContentDraft, ContentType

from shared_core.memory.postgres import PostgresClient

from shared_core.memory.repository import MemoryRepository 

from shared_core.memory.manager import MemoryManager 

console=Console()

def banner():
    console.print(
        Panel.fit(
            "[bold cyan]Content Delivery Agent[/bold cyan]\n"
            "Day 21 • 30 AI Agents in 30 Days",

            title="Publishing Workflow",
        )
    )

def load_markdown():
    return Path("sample.md").read_text()

def main():
    banner()
    postgres=PostgresClient("postgresql://postgres:postgres@localhost:5432/ai_agents")
    repository=MemoryManager(repository)
    agent=CMSPublishingAgent(memory_manager=manager)
    draft=ContentDraft(
        title="Building AI Agents",
        body=load_markdown(),
        content_type=ContentType.BLOG
    )
    with agent.open_authenticated_browser() as page:
        page.goto(
            "https://your-cms.example.com",wait_until="networkidle"
        )

        result = agent.publish(page, draft)

    
    publish=result["publish"]

    table=Table(title="Publishing Result")

    table.add_column("Field",style="cyan")
    table.add_column("Value",style="magenta")

    table.add_row("Status",publish["status"])
    table.add_row("Preview URL",publish["preview_url"])


    console.print(table)

    console.print()

    console.print(

        Panel(

            result["reasoning"],

            title="AI Summary",

        )

    )

if __name__ == "__main__":
    main()