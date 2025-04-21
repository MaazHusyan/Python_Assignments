DAY_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def main():
    print("Count the Tota seconds in year:\n")
    
    user_inp = int(input("Enter Number of year(s): "))

    result = "Year" if user_inp == 1 else "Years" if user_inp > 1 else "Years"# Print years and year 
    
    total_sec = user_inp * DAY_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    
    print(f"There are {total_sec} seconds in {user_inp} {result} ")
    
    
    
if __name__ == '__main__':
    main()