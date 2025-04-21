import random
from _spaghetti import Words
import string

def get_word(word):
    word = random.choice(Words)
    
    while "-" in word or " " in word:
        word = random.choice(Words)
    
    return word.upper()

def hangman():
    word = get_word(Words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = len(word) + 2
    # user input         
    while len(word_letters) > 0 and lives > 0:
        print(f"you have {lives} left and you have used these letters: "," ".join(used_letters)) # join the letters of list like, [a, s, as] => "a s as"
        
        # what the current word is like, D - G
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("current word: "," ".join(word_list))
        
        
        
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("letter is not in word!")
            
        elif user_letter in used_letters:
            print("you have already used that character, try again!")
        else:
            print("invalid character, try again!")
      
    if lives == 0:
        print(f"you ran out of lives, game over  !!!'{word}'")
    else:
        print(f"you have guess the {word} correctly :)")

hangman()