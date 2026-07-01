from rich.console import Console
from rich.panel import Panel

from agent import FileSystemAgent
from sample_commands import COMMANDS

console = Console()


def menu():

    console.print(
        Panel.fit(
            "[bold cyan]Day 6[/bold cyan]\n"
            "CLI File-System Commander",
            title="30 Agents in 30 Days",
        )
    )

    console.print()

    for index, cmd in enumerate(COMMANDS, 1):

        console.print(
            f"{index}. {cmd}"
        )

    console.print(
        f"{len(COMMANDS)+1}. Custom Command"
    )

    console.print(
        f"{len(COMMANDS)+2}. Exit"
    )


def main():

    agent = FileSystemAgent()

    while True:

        menu()

        choice = input(
            "\nChoice > "
        )

        if choice == str(len(COMMANDS) + 2):

            break

        if choice == str(len(COMMANDS) + 1):

            user_input = input(
                "\nCommand > "
            )

        else:

            user_input = COMMANDS[
                int(choice) - 1
            ]

        print()

        print("User:", user_input)

        result = agent.run(
            user_input
        )

        print()

        print(result)

        print("\n")

if __name__ == "__main__":
    main()