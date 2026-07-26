from rich.console import Console 

console=Console()

class AlertManager:
    async def publish(self, alert):
        console.print() 
        console.print("[bold red]ALERT[/bold red]"
        )
        console.print(
            f"[{alert.severity.value.upper()}]"
        )

        console.print(alert.title)

        console.print(alert.description)

