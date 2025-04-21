# Rolling dice!! scope of variables
import random

DICE_SIDES = 6

def roll_dice():
    # roll Two dice & print there total
    die1: int = random.randint(1, DICE_SIDES)
    die2: int = random.randint(1, DICE_SIDES)
    
    total_die = die1 + die2
    
    print(f"Total of two dice is {total_die}")
    
def main():
    die1: int = 10
    print(f"die1 in main() starts as: {str(die1)}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() is: {str(die1)}")
    
if __name__ == "__main__":
    main()