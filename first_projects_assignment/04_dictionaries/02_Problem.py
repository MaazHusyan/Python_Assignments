def addIn_phone_book():
    phone_book = {}

    while True:
        name = input("Name: ").strip()
        
        if name == "":
            break
        number = input("Number: ")
        
        phone_book[name] = number
    return phone_book

def print_phone_book(phone_book):
    
    for name in phone_book:
        print(f"Name: {name} -> {phone_book[name]}")

def check_phone_book(phone_book):
    while True:
        name = input("Enter name to check book: ").strip()
        if name == "":
            break
            
        if name not in phone_book:
            print(f"{name} is not in Phone book")
            break
        else:
            print(f"***{phone_book[name]}*** is saved as ***{name}***")

def main():
    phone_book = addIn_phone_book()
    print_phone_book(phone_book)
    check_phone_book(phone_book)



if __name__ == "__main__":
    main()