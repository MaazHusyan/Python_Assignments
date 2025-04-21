IRAN = 16
UAE = 25
ANTARCTICA = 35


def main():
    age_factor = int(input("Enter age to check eligibility for voting: "))
    # IRAN age 
    if age_factor >= IRAN :
        print(f"You can vote in IRAN, Where the voting age is {IRAN}.")
    else:
        print(f"You can't vote in IRAN, where the voting age is {IRAN}.")
    # UAE age
    if age_factor >= UAE :
        print(f"You can vote in UAE, Where the voting age is {UAE}.")
    else:
        print(f"You can't vote in UAE, where the voting age is {UAE}.")
    # ANTARCTICA age
    if age_factor >= ANTARCTICA :
        print(f"You can vote in ANTARCTICA, Where the voting age is {ANTARCTICA}.")
    else:
        print(f"You can't vote in ANTARCTICA, where the voting age is {ANTARCTICA}.")
    
if __name__ == '__main__':
    main()