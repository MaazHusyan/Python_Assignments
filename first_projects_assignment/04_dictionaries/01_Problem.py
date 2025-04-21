def get_user_nums():
    num_lst = []

    while True:
        user_inp = input("Store a number: ").strip()  # Strip spaces for safety

        if user_inp == "":  # Stop when input is empty
            break

        try:
            num = int(user_inp)
            num_lst.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-numeric input

    return num_lst

def count_nums(num_lst):
    num_dict = {}

    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict

def print_total_counts(num_dict):
    for num in num_dict:
        result = 'time' if num_dict[num] == 1 else 'times'  # Singular/plural correction
        print(f"{num} is stored {num_dict[num]} {result}.")

def main():
    user_num = get_user_nums()
    num_dict = count_nums(user_num)
    print_total_counts(num_dict)

if __name__ == "__main__":
    main()
