def get_first_elm(l_item):
    print(l_item[-1])#print the last item of list
    
def get_list():
    l_item = []
    user_inp = input("Enter an element: ")
    while user_inp != "":
        l_item.append(user_inp)
        user_inp = input("Enter an element or press Enter to stop: ")
    return l_item
    

def main():
    l_item = get_list()
    get_first_elm(l_item)
    
if __name__ == "__main__":
    main()
    