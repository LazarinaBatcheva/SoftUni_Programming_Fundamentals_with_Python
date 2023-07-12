phones_list = [phone for phone in input().split(", ")]
command = input()

while command != "End":
    command = command.split(" - ")
    action = command[0]

    if action == "Add":
        phone = command[1]
        if phone not in phones_list:
            phones_list.append(phone)

    elif action == "Remove":
        phone = command[1]
        if phone in phones_list:
            phones_list.remove(phone)

    elif action == "Bonus phone":
        old_phone, new_phone = command[1].split(":")
        if old_phone in phones_list:
            phones_list.insert(phones_list.index(old_phone) + 1, new_phone)

    elif action == "Last":
        phone = command[1]
        if phone in phones_list:
            phones_list.remove(phone)
            phones_list.append(phone)

    command = input()

print(", ".join(phones_list))