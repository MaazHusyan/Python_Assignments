import random

def play():
    print("\t'r' is rock | 'p' is paper | 's' is scissors ")
    user = input("My Choice is : ").lower()
    computer = random.choice(["r", "p", "s"])
    
    print(f"Computer Choice is : {computer}")
    
    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You win"
        
    return "You lost"
    
def is_win(player, opponent):
    # rock beats scissor | scissor beats paper | paper beats rock
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    
print(play())