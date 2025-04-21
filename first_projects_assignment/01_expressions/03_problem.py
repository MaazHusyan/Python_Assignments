INCHES_IN_FOOT: int = 12
def main():
    feet: int = int(input("Enter number to convert in Inches:\n "))
    # convert to inch
    inches: float = float(feet) * INCHES_IN_FOOT
    
    if feet == 1.0:
        print(f"{feet} foot = {inches} inches")
    else:
        print(f"{feet} feet = {inches} inches")
        
if __name__ == '__main__':
    main()