import sys
from rich.console import Console
from rich.panel import Panel
from hexasafelink.core.scanner import scan_url

console = Console()

def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Usage:[/bold red] hexasafelink <url>")
        sys.exit(1)

    url = sys.argv[1]

    console.print(Panel.fit(
        "[bold cyan]🔐 HexaSafeLink CLI[/bold cyan]\n"
        "Your Shield Against Scam Links",
        border_style="cyan"
    ))

    result = scan_url(url)

    console.print(f"[bold]URL:[/bold] {url}")
    console.print(f"[bold]Domain:[/bold] {result['domain']}")
    console.print(f"[bold]IP:[/bold] {result['ip']}")

    console.print("\n[bold]Findings:[/bold]")
    if result["findings"]:
        for f in result["findings"]:
            console.print(f" • [red]{f}[/red]")
    else:
        console.print(" • [green]No suspicious signs found[/green]")

    color = "green"
    if result["risk_level"] == "SUSPICIOUS":
        color = "yellow"
    elif result["risk_level"] == "HIGH RISK":
        color = "red"

    console.print(
        Panel.fit(
            f"[bold {color}]{result['risk_level']}[/bold {color}]\n"
            f"Risk Score: {result['risk_score']}",
            border_style=color
        )
    )

if __name__ == "__main__":
    main()

