def main():
    list_of_elms = []
    
    user_inp = input("Enter an element: ")
    
    while user_inp:
        list_of_elms.append(user_inp)
        
        user_inp = input("Enter an element or press Enter to stop: ")
    
    print("List: ",list_of_elms)

    


    
    
if __name__ == "__main__":
    main()