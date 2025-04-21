C: int = 299792458 ** 2 # the speed of light in m/s (metres per second)
def main():
    mass_in_kg: float = float(input("Enter a mass(weight) in kg: "))#get the inout from user
    # calculate the energy
    energy_in_joules:float = mass_in_kg * C     
    # display work to user
    print("e = m * C²...")
    print(f"m = {str(mass_in_kg)} kg ")
    print(f"C = {str(C)} m/s")
    
    # display the out come
    print(f"Energy in joules: {energy_in_joules}")
    
    print(f"""
          e = {mass_in_kg}kg * {C}
          -------------------------
          {energy_in_joules} = e """) 
  
  
if __name__ == '__main__':
    main()