AFFIRMATION = "I am capable, I am learning, and I am improving every day."

def main():
    print(f"\nPlease type the following affirmation:\n{AFFIRMATION}")
    
    user_inp = input()
    
    while user_inp != AFFIRMATION:
        print("Thats not the same affirmation.")
        
        print(f"\nPlease type the following affirmation:\n{AFFIRMATION}")
        user_inp = input()
    print("Now, Much better!\nGood to go!")


if __name__ == '__main__':
    main()