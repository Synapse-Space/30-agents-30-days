"""
Day 8 - Conversational Reminder Bot
"""

import threading

from rich.console import Console
from rich.panel import Panel

from agent import ReminderAgent
from sample_chats import SAMPLE_CHATS
from worker import ReminderWorker

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]Conversational Reminder Bot[/bold cyan]\n"
            "Day 8 • AI Agent Challenge",

            title="30 Agents • 30 Days"

        )

    )


def menu():

    banner()

    console.print()

    for i, chat in enumerate(SAMPLE_CHATS, start=1):

        console.print(

            f"{i}. {chat}"

        )

    console.print(

        f"{len(SAMPLE_CHATS)+1}. Custom Reminder"

    )

    console.print(

        f"{len(SAMPLE_CHATS)+2}. Exit"

    )


def start_worker():

    worker = ReminderWorker()

    worker.start()


def main():

    threading.Thread(

        target=start_worker,

        daemon=True,

    ).start()

    agent = ReminderAgent()

    while True:

        menu()

        choice = input(

            "\nChoice > "

        )

        if choice == str(len(SAMPLE_CHATS)+2):

            break

        if choice == str(len(SAMPLE_CHATS)+1):

            message = input(

                "\nYou > "

            )

        else:

            message = SAMPLE_CHATS[int(choice)-1]

            console.print(

                f"\nYou > {message}"

            )

        result = agent.process(

            message

        )

        console.print()

        console.print(

            Panel(

                result["message"],

                title="Assistant"

            )

        )

        if result["type"] == "followup":

            followup = input(

                "\nYou > "

            )

            result = agent.process(

                followup

            )

            console.print(

                Panel(

                    result["message"],

                    title="Assistant"

                )

            )

        input(

            "\nPress ENTER to continue..."

        )


if __name__ == "__main__":

    main()