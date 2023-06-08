line_of_integers = input().split()
line_of_integers_list = [int(number) for number in line_of_integers]

while True:
    command = input()
    if command == "end":
        print(line_of_integers_list)
        break

    new_command = command.split()
    if new_command[0] == "exchange":
        exchange_index = int(new_command[1])
        if exchange_index > (len(line_of_integers_list) - 1) or exchange_index < 0:
            print("Invalid index")
        else:
            line_of_integers_list = (line_of_integers_list[exchange_index + 1:]) + \
                                (line_of_integers_list[:exchange_index + 1])

    even_numbers = []
    odd_numbers = []
    index_list_even = []
    index_list_odd = []
    for number in line_of_integers_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    if new_command[0] == "max" and new_command[1] == "even" and even_numbers:
        for index, element in enumerate(line_of_integers_list):
            if element == max(even_numbers):
                index_list_even.append(index)
        if len(index_list_even) == 1:
            print(index_list_even[0])
        else:
            print(index_list_even[-1])
    elif new_command[0] == "max" and new_command[1] == "odd" and odd_numbers:
        for index, element in enumerate(line_of_integers_list):
            if element == max(odd_numbers):
                index_list_odd.append(index)
        if len(index_list_odd) == 1:
            print(index_list_odd[0])
        else:
            print(index_list_odd[-1])
    elif new_command[0] == "min" and new_command[1] == "even" and even_numbers:
        for index, element in enumerate(line_of_integers_list):
            if element == min(even_numbers):
                index_list_even.append(index)
        if len(index_list_even) == 1:
            print(index_list_even[0])
        else:
            print(index_list_even[-1])
    elif new_command[0] == "min" and new_command[1] == "odd" and odd_numbers:
        for index, element in enumerate(line_of_integers_list):
            if element == min(odd_numbers):
                index_list_odd.append(index)
        if len(index_list_odd) == 1:
            print(index_list_odd[0])
        else:
            print(index_list_odd[-1])
    elif (new_command[0] == "max" or new_command[0] == "min") and (not even_numbers or not odd_numbers):
        print("No matches")

    if new_command[0] == "first" or new_command[0] == "last":
        count_element = int(new_command[1])
        if 0 < count_element <= len(line_of_integers_list):
            if new_command[0] == "first" and new_command[2] == "even":
                if len(even_numbers) < count_element:
                    print(even_numbers)
                else:
                    print(even_numbers[:count_element])
            elif new_command[0] == "first" and new_command[2] == "odd":
                if len(odd_numbers) < count_element:
                    print(odd_numbers)
                else:
                    print(odd_numbers[:count_element])
            elif new_command[0] == "last" and new_command[2] == "even":
                if len(even_numbers) < count_element:
                    print(even_numbers)
                else:
                    print(even_numbers[-count_element:])
            elif new_command[0] == "last" and new_command[2] == "odd":
                if len(odd_numbers) < count_element:
                    print(odd_numbers)
                else:
                    print(odd_numbers[-count_element:])
        else:
            print("Invalid count")