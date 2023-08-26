command = input()
phonebook_dict = {}

while command != "Over":
    name, number = command.split(" : ")
    if name.isdigit():
        name, number = number, name
    if name not in phonebook_dict.keys():
        phonebook_dict[name] = ""
    phonebook_dict[name] = number
    command = input()

for name, number in sorted(phonebook_dict.items()):
    print(f"{name} -> {number}")