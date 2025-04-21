def get_first_elm(f_item):
    print(f_item[0])#print the first item of list
    
def get_list():
    f_item = []
    user_inp = input("Enter first element: ")
    while user_inp != "":
        f_item.append(user_inp)
        user_inp = input("Enter an element or press Enter to stop: ")
    return f_item
    

def main():
    f_item = get_list()
    get_first_elm(f_item)
    
if __name__ == "__main__":
    main()
    