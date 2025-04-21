import random

RANGE_NUM = 10
MIN_VAL = 1
MAX_VAL = 100

def main():
    for _ in range(RANGE_NUM):
        num = random.randint(MIN_VAL, MAX_VAL)
        print(num,end=", ")
       
if __name__ == '__main__':
    main()
        
        