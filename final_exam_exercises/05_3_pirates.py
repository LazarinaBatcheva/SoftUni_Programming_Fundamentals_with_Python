def plundering_a_city(current_action, cities_info):
    city, people, gold = current_action[1], int(current_action[2]), int(current_action[3])
    cities_info[city]["population"] -= people
    cities_info[city]["gold"] -= gold
    print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities_info[city]["population"] <= 0 or cities_info[city]["gold"] <= 0:
        print(f"{city} has been wiped off the map!")
        del cities_info[city]
    return cities_info


def prosper_city(current_action, cities_info):
    city, gold = current_action[1], int(current_action[2])
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities_info[city]["gold"] += gold
        print(f"{gold} gold added to the city treasury. "
              f"{city} now has {cities_info[city]['gold']} gold.")
    return cities_info


def base_function(current_command, cities_info):
    while current_command != "End":
        action = current_command.split("=>")
        if action[0] == "Plunder":
            cities_info = plundering_a_city(action, cities_info)
        elif action[0] == "Prosper":
            cities_info = prosper_city(action, cities_info)
        current_command = input()
    if cities_info:
        print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
        for city in cities_info:
            print(f"{city} -> Population: {cities_info[city]['population']} "
                  f"citizens, Gold: {cities_info[city]['gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def creating_cities_dict(current_command):
    cities_info = dict()
    while current_command != "Sail":
        city, population, gold = current_command.split("||")
        if city not in cities_info.keys():
            cities_info[city] = {"population": int(population), "gold": int(gold)}
        else:
            cities_info[city]["population"] += int(population)
            cities_info[city]["gold"] += int(gold)
        current_command = input()
    return cities_info


command = input()
cities_dict = creating_cities_dict(command)
new_command = input()
base_function(new_command, cities_dict)