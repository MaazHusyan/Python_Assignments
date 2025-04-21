import random

def main(x_num)->str:
    random_num: int = random.randint(1, x_num)
    
    guess = 0
    
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 - {x_num} :"))
        
        if guess < random_num:
            print("Too low, Guess again !")
        elif guess > random_num:
            print("Too high, Guess again !")
            
    print(f"Congrats right number is {random_num}")

main(99999)