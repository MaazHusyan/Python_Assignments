import secrets

chars:str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?/;:1234567890"

user_number:int = int(input("How many passwords do you want?: "))

pass_length:int = int(input("Enter the length of your password: "))

for p in range(user_number):
    passwords:str = ""
    
    for c in range(pass_length):
        passwords += secrets.choice(chars)
    
    print(f"Password: {passwords}")