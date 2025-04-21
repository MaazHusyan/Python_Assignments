# Area of Triangle
from rich.console import Console

console = Console()
def main():
    side_1:float = float(input("Enter the length of first side: "))
    side_2:float = float(input("Enter the length of second side: "))
    side_3:float = float(input("Enter the length of third side: "))
    
    total_area = side_1 + side_2 + side_3
    
    console.print(f"[bold]Total area of Triangle is {str(total_area)}[/bold]")
    
if __name__ == "__main__":
    main()