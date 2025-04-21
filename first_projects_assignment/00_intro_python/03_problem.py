# Degree ℉ to ℃
from rich.console import Console

console = Console()
def main():    
    degrees_fahrenheit: str = console.input("[bold] Enter temp in Fahrenheit:[/bold] ")

    degrees_fahrenheit: float = float(degrees_fahrenheit)
    
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    
    console.print(f"[bold italic] Temperature: {degrees_celsius:.2f} ℃ [/bold italic]")
    
if __name__ == '__main__':
    main()