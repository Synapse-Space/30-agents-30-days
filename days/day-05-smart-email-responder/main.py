
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import EmailAssistantAgent
from sample_emails import EMAILS

console = Console()


def show_menu():

    console.print(
        Panel.fit(
            "[bold cyan]Smart Email Assistant[/bold cyan]\n"
            "Classify • Analyze • Draft Replies",
            title="Day 5",
        )
    )

    console.print("1. Support Email")
    console.print("2. Sales Email")
    console.print("3. Spam Email")
    console.print("4. General Email")
    console.print("5. Bug Report (Yuvraj)")
    console.print("6. Enterprise Pricing (Gurkirtan)")
    console.print("7. App Feature Query (Aniket)")
    console.print("8. Enter Custom Email")
    console.print("9. Exit")


def custom_email():

    console.print("\nPaste the email below.")
    console.print("Press ENTER twice to finish.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    return "\n".join(lines)


def print_result(result):

    table = Table(title="Analysis")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Intent", result.intent)
    table.add_row("Priority", result.priority)
    table.add_row("Sentiment", result.sentiment)
    table.add_row("Confidence", f"{result.confidence:.2f}")
    table.add_row("Summary", result.summary)

    console.print(table)

    console.print(
        Panel(
            Markdown(result.draft_response),
            title="Draft Reply",
        )
    )


def main():

    agent = EmailAssistantAgent()

    while True:

        show_menu()

        choice = input("\nChoice > ").strip()

        if choice == "9":

            console.print(
                "\n👋 Goodbye!"
            )

            break

        if choice == "8":

            email = custom_email()

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:

            email = EMAILS[int(choice) - 1]

        else:

            console.print(
                "[red]Invalid option.[/red]"
            )

            continue

        console.print(
            Panel(
                email,
                title="Incoming Email",
            )
        )

        try:

            result = agent.process(email)

            print_result(result)

        except Exception as exc:

            console.print(
                f"[bold red]{exc}[/bold red]"
            )


if __name__ == "__main__":
    main()