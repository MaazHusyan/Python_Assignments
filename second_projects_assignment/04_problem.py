import random

def main():
    random_num = random.randint(0,10)
    while True:
        user_inp = int(input("Guess the number between 1-10: "))
        
        if user_inp < random_num:
            print("Your guess is too low")
        elif user_inp > random_num:
            print("Your guess is too high")
        else:
            print(f"Congrates! the number is {random_num}")
            break
        
if __name__ == "__main__":
    main()