"""
Day 3 - Structured Data Extractor

Run:
    python main.py
"""

from rich.console import Console
from rich.json import JSON
from rich.panel import Panel

from agent import StructuredExtractorAgent
from sample_emails import EMAILS


console = Console()


def display_menu() -> None:
    """Display the available options."""

    console.print(
        Panel.fit(
            "[bold cyan]Structured Data Extractor[/bold cyan]\n"
            "Extract structured information from unstructured emails.",
            title="Day 3",
        )
    )

    console.print("\nChoose an option:")
    console.print("1. Sample Email #1")
    console.print("2. Sample Email #2")
    console.print("3. Sample Email #3")
    console.print("4. Enter Custom Email")
    console.print("5. Exit")


def get_email(choice: str) -> str | None:
    """Return email text based on user selection."""

    if choice == "1":
        return EMAILS[0]

    if choice == "2":
        return EMAILS[1]

    if choice == "3":
        return EMAILS[2]

    if choice == "4":

        console.print(
            "\nPaste your email below."
        )

        console.print(
            "Finish by entering an empty line.\n"
        )

        lines = []

        while True:

            line = input()

            if line == "":
                break

            lines.append(line)

        return "\n".join(lines)

    return None


def main():

    agent = StructuredExtractorAgent()

    while True:

        display_menu()

        choice = input("\nChoice > ").strip()

        if choice == "5":

            console.print(
                "\n👋 Goodbye!"
            )

            break

        email = get_email(choice)

        if email is None:

            console.print(
                "[red]Invalid option.[/red]"
            )

            continue

        console.print(
            Panel(
                email,
                title="Input Email",
            )
        )

        try:

            result = agent.run(email)

            console.print(
                "\n[bold green]Extraction Successful[/bold green]\n"
            )

            console.print(
                JSON.from_data(
                    result.model_dump()
                )
            )

        except Exception as exc:

            console.print(
                f"[bold red]{exc}[/bold red]"
            )


if __name__ == "__main__":
    main()