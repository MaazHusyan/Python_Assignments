# favorite animal is same
from rich.console import Console

console = Console()
def main():
    print("This program ask a question!!\n")
    
    user_inp: str = console.input("[bold]What's your favorite animal?[/bold] ")
    
    console.print(f"[bold italic]My favorite animal is also {user_inp}![/bold italic] ")

if __name__ == '__main__':
    main()