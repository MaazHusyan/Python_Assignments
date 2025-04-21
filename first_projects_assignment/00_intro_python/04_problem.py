# Find the age
from rich.console import Console

console = Console()
def main():
    Anton: int = 21
    Beth : int = 6 + Anton
    Chen : int = 20 + Beth
    Drew : int = Chen + Anton
    Ethan : int = Chen
    
    # print
    console.print(str(f"[bold]Anton is {Anton}[/bold]"))
    console.print(str(f"[bold]Beth is {Beth}[/bold]"))
    console.print(str(f"[bold]Chen is {Chen}[/bold]"))
    console.print(str(f"[bold]Drew is {Drew}[/bold]"))
    console.print(str(f"[bold]Ethen is {Ethan}[/bold]"))
    
    
    
if __name__ == '__main__':
    main()