items = {"shards": 0, "fragments": 0, "motes": 0}
current_item = input().split()
obtained = False

while not obtained:
    for index in range(0, len(current_item), 2):
        key = current_item[index + 1].lower()
        value = int(current_item[index])
        if key not in items.keys():
            items[key] = 0
        items[key] += value

        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    current_item = input().split()

for material, quantity in items.items():
    print(f"{material}: {quantity}")