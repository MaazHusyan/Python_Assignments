import random

def main():
    random_num = random.randint(1, 99)
    
    
    while True:
        
        print("\nCan U guess tne number a between 1 - 99?")
        
        guess_num = int(input("Guess: "))

        if guess_num == random_num:
            print("Congrates U guess the right number.")
            break
        
        elif guess_num < random_num:
            print("No, Your guess is too low,\nTry again...")
        
        elif guess_num > random_num:
            print("No, Your guess is too high,\nTry again...")
            









if __name__ == '__main__':
    main()