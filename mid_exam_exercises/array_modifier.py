elements = [int(element) for element in input().split()]
command = input()

while command != "end":
    current_command = command.split()
    if current_command[0] == "swap":
        index_1, index_2 = int(current_command[1]), int(current_command[2])
        elements[index_1], elements[index_2] = elements[index_2], elements[index_1]
    elif current_command[0] == "multiply":
        index_1, index_2 = int(current_command[1]), int(current_command[2])
        elements[index_1] *= elements[index_2]
    elif current_command[0] == "decrease":
        elements = [element - 1 for element in elements]

    command = input()
print(*elements, sep=", ")