shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":

    if "Correct" in command:
        command, old_item, new_item = command.split()
        if old_item in shopping_list:
            shopping_list[shopping_list.index(old_item)] = new_item
        command = input()
        continue

    command, item = command.split()

    if command == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif command == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)

    elif command == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

    command = input()

print(", ".join(shopping_list))