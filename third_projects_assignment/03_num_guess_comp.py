import random

def main(x):
    low = 1
    high = x
    feedback = ""
    
    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(f"If {guess} is high(H), low(L) or correct(C) :").lower()
        
        if feedback == "h":
            high = guess - 1
            
        elif feedback == "l": 
            low = guess + 1
        
    print("Computer wins ...")
    
main(100)