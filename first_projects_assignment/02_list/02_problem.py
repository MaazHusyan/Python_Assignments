def main():
    numbers:list[int] = [1, 2, 3, 4, 5]
    print(numbers)
    for i in range(len(numbers)):
        elm_index = numbers[i]
        numbers[i] = elm_index * 2
    
    print(numbers)

if __name__ == '__main__':
    main()