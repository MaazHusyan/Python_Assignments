REQUIRED_HEIGHT = 45

def main():
    height = int(input("Chech Height: "))
    
    while height:
        if height < REQUIRED_HEIGHT:
            print("You are short, NEXT...") 
            height = int(input("Chech Height: ")) 
            if height >= REQUIRED_HEIGHT:
                print("You are tall enough to ride.")
                break
        else: break
        
if __name__ == "__main__":
    main()