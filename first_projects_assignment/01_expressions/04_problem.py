import math
def main():
    ab: float = float(input("Enter the length of side AB: "))# get the length of ab from user
    ac: float = float(input("Enter the length of side AC: "))# get the length of ac from user
    
    bc: float = math.sqrt(ab**2 + ac**2)
    
    print(f"The length of BC (hypotenuse) is: {bc:.3f}")
    
if __name__ == "__main__":
    main()