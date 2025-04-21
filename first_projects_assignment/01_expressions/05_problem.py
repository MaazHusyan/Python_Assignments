def main():
    # Get user input for dividend and divisor
    dividend: int = int(input("Enter the number to be divided (dividend): "))   
    divisor: int = int(input("Enter the number to divide by (divisor): "))   

    # Check for division by zero
    if divisor == 0:
        print("Error: Division by zero is not allowed.")
        return  # Exit the function to prevent further execution

    # Calculate quotient and remainder
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    # Display results
    print(f"If {dividend} is divided by {divisor}:")
    print(f"- Quotient (whole number result) = {quotient}")
    print(f"- Remainder = {remainder}")

if __name__ == '__main__':
    main()
