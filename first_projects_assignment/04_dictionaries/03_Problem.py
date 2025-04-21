def main():
    fruits_rate_list = {
        "apple": 2,
        "banana": 4.1,
        "grapes": 3.6,
        "star fruit": 6,
        "malon": 10,
        "orange": 3
    }
    
    total_amount = 0
    for fruits in fruits_rate_list:
        fruit_price = fruits_rate_list[fruits]
        fruit_count = input(f"How many {fruits} do you want? : ")
        
        total_amount += float(fruit_price) * int(fruit_count)
    
    print(f"Your total amount is {total_amount}₨")
        


if __name__ == '__main__':
    main()