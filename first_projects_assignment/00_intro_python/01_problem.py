# sum of two
from rich.console import Console

console = Console()
def main():
    print("This program adds two numbers!!\n")
    
    num1: str = console.input("[bold]Enter first number:[/bold] ")  
    num1: int = int(num1) 
    num2: str = console.input("[bold]Enter second number:[/bold] ")  
    num2: int = int(num2) 
    
    Total = num1 + num2
    
    console.print(f"[bold italic]The total is:[/bold italic] {str(Total)}")
    
if __name__ == '__main__':
    main()