import random
DISE_SIDES = 6
def main():
   die_1 = random.randint(0, DISE_SIDES)
   die_2 = random.randint(0, DISE_SIDES)
   
   dice_total = die_1 + die_2
   
   print(f"Each dice have {DISE_SIDES} sides ")
   print(f"First dice: {die_1}")
   print(f"Second dice: {die_2}")
   print(f"Total of two dice: {dice_total}")
   
if __name__ == '__main__':
    main()