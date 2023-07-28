command = input()
guests = {}
unliked_meals = 0

while command != "Stop":
    action, guest_name, meal = command.split("-")
    if action == "Like":
        if guest_name not in guests.keys():
            guests[guest_name] = []
        if meal not in guests[guest_name]:
            guests[guest_name].append(meal)

    elif action == "Unlike":
        if guest_name not in guests.keys():
            print(f"{guest_name} is not at the party.")
        else:
            if meal in guests[guest_name]:
                guests[guest_name].remove(meal)
                print(f"{guest_name} doesn't like the {meal}.")
                unliked_meals += 1
            else:
                print(f"{guest_name} doesn't have the {meal} in his/her collection.")
    command = input()

sorted_guests = sorted(guests.items(), key=lambda x: (-len(x[1]), x[0]))
for guest, meals in sorted_guests:
    sorted_meals = sorted(meals)
    print(f"{guest}: {', '.join(sorted_meals)}")
print(f"Unliked meals: {unliked_meals}")