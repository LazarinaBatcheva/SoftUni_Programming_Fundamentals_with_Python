def check_for_plant(plant_name):
    if plant_name in plants_info:
        return True
    print("error")


def rate_plant(plant_information):
    if check_for_plant(plant_name):
        plant_information[plant_name][1].append(rating)


def update_info(plant_information):
    if check_for_plant(plant_name):
        plant_information[plant_name][0] = new_rarity


def reset_info(plant_information):
    if check_for_plant(plant_name):
        plant_information[plant_name][1] = []


def result():
    print("Plants for the exhibition:")
    for plant in plants_info:
        average_rating = 0
        if sum(plants_info[plant][1]) > 0:
            average_rating = sum(plants_info[plant][1]) / len(plants_info[plant][1])
        print(f"- {plant}; Rarity: {plants_info[plant][0]}; Rating: {average_rating:.2f}")


number_of_lines = int(input())
plants_info = dict()
for current_plant in range(number_of_lines):
    plant_name, rarity = input().split("<->")
    plants_info[plant_name] = [rarity, []]

command = input()
while command != "Exhibition":
    if "Rate" in command:
        command = command.split(": ")[1].split(" - ")
        plant_name, rating = command[0], int(command[1])
        rate_plant(plants_info)
    elif "Update" in command:
        command = command.split(": ")[1].split(" - ")
        plant_name, new_rarity = command[0], int(command[1])
        update_info(plants_info)
    elif "Reset" in command:
        plant_name = command.split(": ")[1]
        reset_info(plants_info)
    command = input()

result()
