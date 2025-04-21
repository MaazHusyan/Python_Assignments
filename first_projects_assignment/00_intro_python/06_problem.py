# Here is the Square root
from rich.console import Console

console = Console()
def main():
    print("This program prints the Square of user's given number\n ")
    user_inp: int = console.input("[bold]Enter a number to calculate its square: [/bold]")

    console.print(f"[bold]{int(user_inp)}² = {int(user_inp) ** 2}[/bold]")



if __name__ == "__main__":
    main()