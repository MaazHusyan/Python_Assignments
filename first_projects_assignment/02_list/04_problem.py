
def add_three(list_of_elms, data):
    for i in range(3):
        list_of_elms.append(data)
    
def main():
    user_inp = input("Enter a massege: ")
    list_of_elms = []
    print("Original list: ",list)
    add_three(list_of_elms, user_inp)
    print("Modified list: ",list_of_elms)
    
    
if __name__ == '__main__':
    main()