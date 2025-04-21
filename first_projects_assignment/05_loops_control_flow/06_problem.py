MAX_VALUE = 100 

def main():
    current_val = int(input("Enter a number(Under 100): "))
    
    while current_val < MAX_VALUE:
        current_val = current_val * 2
        print(current_val)
        
main()