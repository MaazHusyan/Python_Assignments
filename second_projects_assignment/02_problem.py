MAX_VALUE = 100
def main():
    user_inp = int(input("Enterr a number: "))
    
    while user_inp < MAX_VALUE:
        user_inp = user_inp *2
        print(user_inp)
        
if __name__ == "__main__":
    main()