MAX_LENGTH = 3
def shorten(lst):
    
    while len(lst) >= MAX_LENGTH:
        last_items = lst.pop()
        print(last_items)
        
def get_items():
    lst = []
    
    user_inp = input("Please enter an element of the list or press enter to stop: ")
    
    while user_inp != "":
        lst.append(user_inp)
        user_inp = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_items()
    shorten(lst)
    
if __name__ == "__main__":
    main()