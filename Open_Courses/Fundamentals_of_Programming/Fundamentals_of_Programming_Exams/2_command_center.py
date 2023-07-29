def swap_elements(int_list, index1, index2, action_counter):
    if 0 <= index1 < len(int_list) and 0 <= index2 < len(int_list):
        int_list[index1], int_list[index2] = int_list[index2], int_list[index1]
    print(int_list)
    action_counter += 1
    return action_counter


def enumerate_list(int_list, action_counter):
    enumerated_list = list(enumerate(int_list))
    print(enumerated_list)
    action_counter += 1
    return action_counter


def found_max_number(int_list, action_counter):
    print(max(int_list))
    action_counter += 1
    return action_counter


def found_min_number(int_list, action_counter):
    print(min(int_list))
    action_counter += 1
    return action_counter


def division_result(int_list, division_number, action_counter):
    show_list = []
    for number in int_list:
        if number % division_number == 0:
            show_list.append(number)
    print(show_list)
    action_counter += 1
    return action_counter


def base_function(int_list, current_command, action_counter):
    while current_command != "end":
        action = current_command.split()
        if action[0] == "swap":
            index1 = int(action[1])
            index2 = int(action[2])
            action_counter = swap_elements(int_list, index1, index2, action_counter)
        elif action[0] == "enumerate_list":
            action_counter = enumerate_list(int_list, action_counter)
        elif action[0] == "max":
            action_counter = found_max_number(int_list, action_counter)
        elif action[0] == "min":
            action_counter = found_min_number(int_list, action_counter)
        elif action[0] == "get_divisible":
            division_number = int(action[2])
            action_counter = division_result(int_list, division_number, action_counter)
        current_command = input()
    print(action_counter)


integers = [int(number) for number in input().split()]
command = input()
counter = 0
base_function(integers, command, counter)