phonebook = {}

while True:
    registration = input()
    if "-" not in registration:
        break

    name, phone_number = registration.split("-")
    phonebook[name] = phone_number

for search in range(int(registration)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")