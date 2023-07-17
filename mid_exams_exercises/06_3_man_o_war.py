pirate_ship_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
maximum_health = int(input())
command = input()

while command != "Retire":
    if command == "Status":
        selections_for_repair = 0
        for section in pirate_ship_status:
            if section < (maximum_health * 0.2):
                selections_for_repair += 1
                continue
        print(f"{selections_for_repair} sections need repair.")

    command, *data = command.split()

    if command == "Fire":
        index, damage = int(data[0]), int(data[1])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif command == "Defend":
        star_index, end_index, damage = int(data[0]), int(data[1]), int(data[2])
        if 0 <= star_index < len(pirate_ship_status) and 0 < end_index < len(pirate_ship_status):
            for index in range(star_index, end_index + 1):
                pirate_ship_status[index] -= damage
                if pirate_ship_status[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif command == "Repair":
        index, health = int(data[0]), int(data[1])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > maximum_health:
                pirate_ship_status[index] = maximum_health

    command = input()

print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")