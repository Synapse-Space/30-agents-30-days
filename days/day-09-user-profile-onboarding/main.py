from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agent import OnboardingAgent

console = Console()


def banner():

    console.print(

        Panel.fit(

            "[bold cyan]User Profile Onboarding Agent[/bold cyan]\n"
            "Day 9 • 30 AI Agents in 30 Days",

            title="Workflow Agent",

        )

    )


def print_profile(profile):

    table = Table(title="User Profile")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row(
        "Full Name",
        profile.full_name,
    )

    table.add_row(
        "Email",
        profile.email,
    )

    table.add_row(
        "Phone",
        profile.phone,
    )

    table.add_row(
        "Country",
        profile.country,
    )

    table.add_row(
        "Completed",
        "✅ Yes",
    )

    console.print(table)


def main():

    banner()

    agent = OnboardingAgent()

    console.print()

    console.print(

        Panel(

            agent.current_prompt(),

            title="Assistant",

        )

    )

    while True:

        user_input = input("\nYou > ")

        result = agent.process(
            user_input
        )

        if not result["success"]:

            console.print()

            console.print(

                Panel(

                    result["message"],

                    title="Validation Error",

                    border_style="red",

                )

            )

            console.print()

            console.print(

                Panel(

                    result["next_prompt"],

                    title="Assistant",

                )

            )

            continue

        if result["completed"]:

            console.print()

            console.print(

                Panel.fit(

                    "🎉 Profile Successfully Created",

                    border_style="green",

                )

            )

            print_profile(
                result["profile"]
            )

            break

        console.print()

        console.print(

            Panel(

                result["next_prompt"],

                title="Assistant",

            )

        )


if __name__ == "__main__":

    main()