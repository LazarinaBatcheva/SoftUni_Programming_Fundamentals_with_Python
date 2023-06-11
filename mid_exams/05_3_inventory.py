collecting_items = input().split(", ")
command = input()

while command != "Craft!":
    current_command, item = command.split(" - ")

    if current_command == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)

    elif current_command == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)

    elif current_command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collecting_items:
            old_item_index = collecting_items.index(old_item)
            collecting_items.insert(old_item_index + 1, new_item)

    elif current_command == "Renew":
        if item in collecting_items:
            item = collecting_items.pop(collecting_items.index(item))
            collecting_items.append(item)

    command = input()

print(", ".join(collecting_items))