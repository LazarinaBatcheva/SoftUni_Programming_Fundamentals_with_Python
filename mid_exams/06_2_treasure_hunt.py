treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command, *items = [x for x in command.split()]

    if command == "Loot":
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif command == "Drop":
        index = int(items[0])
        if 0 <= index < len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(index))

    elif command == "Steal":
        count = int(items[0])
        stolen_items = treasure_chest[-count:]
        treasure_chest = treasure_chest[:-count]
        print(", ".join(stolen_items))

    command = input()

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")