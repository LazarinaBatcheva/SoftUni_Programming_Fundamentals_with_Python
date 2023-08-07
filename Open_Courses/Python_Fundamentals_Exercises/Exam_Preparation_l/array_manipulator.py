def exchanging_sub_arrays(action, numbers_list):
    index = int(action[1])
    if 0 <= index < len(numbers_list):
        numbers_list = numbers_list[index + 1:] + numbers_list[:index + 1]
    else:
        print("Invalid index")
    return numbers_list


def finding_max_index_even_odd_number(action, numbers_list):
    even_odd = action[1]
    if even_odd == "even":
        even_numbers = [number for number in numbers_list if number % 2 == 0]
        if even_numbers:
            max_even = max(even_numbers)
            max_number_index = len(numbers_list) - numbers_list[::-1].index(max_even) - 1
            print(max_number_index)
        else:
            print("No matches")
    else:
        odd_numbers = [number for number in numbers_list if number % 2 != 0]
        if odd_numbers:
            max_odd = max(odd_numbers)
            max_number_index = len(numbers_list) - numbers_list[::-1].index(max_odd) - 1
            print(max_number_index)
        else:
            print("No matches")


def finding_min_index_even_odd_number(action, numbers_list):
    even_odd = action[1]
    if even_odd == "even":
        even_numbers = [number for number in numbers_list if number % 2 == 0]
        if even_numbers:
            min_even = min(even_numbers)
            min_number_index = len(numbers_list) - numbers_list[::-1].index(min_even) - 1
            print(min_number_index)
        else:
            print("No matches")
    else:
        odd_numbers = [number for number in numbers_list if number % 2 != 0]
        if odd_numbers:
            min_odd = min(odd_numbers)
            min_number_index = len(numbers_list) - numbers_list[::-1].index(min_odd) - 1
            print(min_number_index)
        else:
            print("No matches")


def finding_first_even_odd_number(action, numbers_list):
    count = int(action[1])
    even_odd = action[2]
    if count > len(numbers_list):
        print("Invalid count")
    else:
        if even_odd == "even":
            even_numbers = [number for number in numbers_list if number % 2 == 0]
            if even_numbers:
                if count > len(even_numbers):
                    print(even_numbers)
                else:
                    print(even_numbers[:count])
            else:
                print([])
        else:
            odd_numbers = [number for number in numbers_list if number % 2 != 0]
            if odd_numbers:
                if count > len(odd_numbers):
                    print(odd_numbers)
                else:
                    print(odd_numbers[:count])
            else:
                print([])


def finding_last_even_odd_number(action, numbers_list):
    count = int(action[1])
    even_odd = action[2]
    if count > len(numbers_list):
        print("Invalid count")
    else:
        if even_odd == "even":
            even_numbers = [number for number in numbers_list if number % 2 == 0]
            if even_numbers:
                if count > len(even_numbers):
                    print(even_numbers)
                else:
                    print(even_numbers[-count:])
            else:
                print([])
        else:
            odd_numbers = [number for number in numbers_list if number % 2 != 0]
            if odd_numbers:
                if count > len(odd_numbers):
                    print(odd_numbers)
                else:
                    print(odd_numbers[-count:])
            else:
                print([])


def base_function(numbers_list):
    command = input()
    while command != "end":
        action = command.split()
        if action[0] == "exchange":
            numbers_list = exchanging_sub_arrays(action, numbers_list)
        elif action[0] == "max":
            finding_max_index_even_odd_number(action, numbers_list)
        elif action[0] == "min":
            finding_min_index_even_odd_number(action, numbers_list)
        elif action[0] == "first":
            finding_first_even_odd_number(action, numbers_list)
        elif action[0] == "last":
            finding_last_even_odd_number(action, numbers_list)
        command = input()
    print(numbers_list)


numbers = [int(number) for number in input().split()]
base_function(numbers)