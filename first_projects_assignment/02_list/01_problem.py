def main():
    numbers: list[int] = [11 , 78, 12]
    
    def add_nums(numbers)-> int:
        total = 0
        for number in numbers:
            total += number
        return total
    
    
    sum_of_nums = add_nums(numbers)

    print(f"The total of numbers is: {sum_of_nums}")


if __name__ == '__main__':
    main()