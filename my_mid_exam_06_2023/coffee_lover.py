coffees_list = [coffee for coffee in input().split()]
number_of_commands = int(input())

for coffee in range(number_of_commands):
    command = input().split()
    action = command[0]

    if action == "Include":
        coffee_type = command[1]
        coffees_list.append(coffee_type)

    elif action == "Remove":
        first_last_coffee = command[1]
        numbers_of_coffees = int(command[2])
        if 0 < numbers_of_coffees < len(coffees_list):
            if first_last_coffee == "first":
                coffees_list = coffees_list[numbers_of_coffees:]
            elif first_last_coffee == "last":
                coffees_list = coffees_list[:-numbers_of_coffees]

    elif action == "Prefer":
        first_index, second_index = int(command[1]), int(command[2])
        if 0 <= first_index < len(coffees_list) and 0 <= second_index < len(coffees_list):
            coffees_list[first_index], coffees_list[second_index] = \
                coffees_list[second_index], coffees_list[first_index]

    elif action == "Reverse":
        coffees_list.reverse()

print("Coffees:")
print(" ".join(coffees_list))