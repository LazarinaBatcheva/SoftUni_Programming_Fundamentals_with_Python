elements = input().split()
command = input()

number_of_moves = 0

while command != "end":
    new_command = [int(x) for x in command.split()]
    first_index = new_command[0]
    second_index = new_command[1]
    number_of_moves += 1
    # check if player try to cheat
    if first_index == second_index or \
            first_index < 0 or first_index > len(elements) - 1 or\
            second_index < 0 or second_index > len(elements) - 1:
        half_sequence_of_elements = int(len(elements) / 2)
        element_to_insert = f"-{number_of_moves}a"
        elements = elements[:half_sequence_of_elements] + \
                   [element_to_insert, element_to_insert] + elements[half_sequence_of_elements:]
        print("Invalid input! Adding additional elements to the board")

    # check for matching elements
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        remove_from_list = elements[first_index]
        elements.remove(remove_from_list)
        elements.remove(remove_from_list)

    else:
        print("Try again!")

    # check if winner
    if len(elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break
    command = input()

if command == "end":
    print("Sorry you lose :(")
    print(*elements, sep=" ")