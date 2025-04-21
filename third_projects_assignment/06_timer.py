import time

def count_time(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
    print("time ends!")
    
user_t = input("Enter time in seconds : ")
count_time(int(user_t))