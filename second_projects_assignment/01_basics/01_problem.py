PROMPT = "What do you want? "

JOKE ="GIAIC GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"

SORRY = "Sorry I only tell jokes"

def main():
    user_inp = input(PROMPT).lower().strip()
    
    if user_inp == "joke":
        print(f"Here is a Joke for you! {JOKE}")
    else:
        print(SORRY)


if __name__ == "__main__":
    main()