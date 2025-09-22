import os
from rich.console import Console
from pyterminal.engine import run_command
from pyterminal.nlp import parse_nlp

console = Console()

def main():
    console.print("[bold magenta]Welcome to PyTerm[/bold magenta] 🚀")
    console.print("Type 'help' for commands. Type 'exit' to quit.\n")

    current_dir = os.getcwd()

    while True:
        # prompt
        console.print(f"[cyan]pyterm:[/cyan] [green]{current_dir}[/green] $ ", end="")
        user_input = input().strip()

        if not user_input:
            continue

        # NLP parser
        parsed_command = parse_nlp(user_input)

        output, current_dir = run_command(parsed_command, current_dir)

        if output == "exit":
            console.print("[bold red]Exiting PyTerm... Goodbye![/bold red]")
            break
        else:
            console.print(f"[yellow]{output}[/yellow]")

if __name__ == "__main__":
    main()
