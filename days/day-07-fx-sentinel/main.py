from rich.console import Console 
from rich.panel import Panel 
from rich.table import Table 

from agent import FXSentinelAgent
from sample_rules import WATCH_RULES

console=Console()

def print_banner():

    console.print(

        Panel.fit(

            "[bold cyan]FX Sentinel[/bold cyan]\n"
            "Day 7 • Currency Monitor",

            title="30 Agents • 30 Days",

        )

    )


def display(result):

    table = Table(title="Market Status")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row(
        "Current Rate",
        str(result["current_rate"]),
    )

    table.add_row(
        "Alert Triggered",
        "✅ YES" if result["alert"] else "❌ NO",
    )

    if result["previous"]:

        table.add_row(
            "Previous Rate",
            str(result["previous"]["last_rate"]),
        )

    console.print(table)


def main():

    agent = FXSentinelAgent()

    while True:

        print_banner()

        console.print()

        for i, rule in enumerate(WATCH_RULES, start=1):

            console.print(

                f"{i}. "

                f"{rule['base']} → {rule['target']}"

            )

        console.print(

            f"{len(WATCH_RULES)+1}. Exit"

        )

        choice = input(

            "\nChoice > "

        )

        if choice == str(len(WATCH_RULES) + 1):

            break

        rule = WATCH_RULES[int(choice) - 1]

        context = agent.load_context()

        result = agent.monitor(

            context=context,

            base=rule["base"],

            target=rule["target"],

            threshold=rule["threshold"],

            direction=rule["direction"],

        )

        display(result)

        print()

        if result["alert"]:

            console.print(

                Panel.fit(

                    "[bold red]ALERT[/bold red]\n"
                    f"{rule['base']}/{rule['target']} crossed the threshold.",

                    title="Notification",

                )

            )

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()