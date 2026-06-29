from rich.console import Console 
from rich.panel import Panel 
from rich.table import Table 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import SQLAgent
console=Console()


def print_results(rows):
    if not rows:
        console.print("[yellow]No rows returned. [/yellow]")

        return
    
    table =Table(show_header=True)

    for column in rows[0].keys():
        table.add_column(column)

    for row in rows:
        table.add_row(*[str(value) for value in row.values()])

    console.print(table)

def main():
    console.print(
        Panel.fit(
            "[bold cyan]Day 4[/bold cyan]\n"
            "Natural Language → SQL Agent",
            title="30 Agents in 30 Days",
        )
    )

    console.print(
        "\n Type 'exit' to quit. \n"
    )
    agent =SQLAgent()

    while True:
        question = input("You > ")

        if question.lower() in ["exit", "quit"]:
            break
        
        try:
            result=agent.run(question)
            console.print(
                Panel(
                    result["explanation"],
                    title="Explanation",
                )
            )

            print_results(
                result["rows"]
            )
        except Exception as exc:
            console.print(
                f"[bold red]{exc}[/bold red]"
            )

if __name__=="__main__":
    main()