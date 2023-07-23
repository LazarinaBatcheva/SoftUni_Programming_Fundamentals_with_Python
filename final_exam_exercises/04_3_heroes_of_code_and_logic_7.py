def casting_spell(heroes, current_command):
    current_hero_name = current_command[1]
    mana_points_needed = int(current_command[2])
    spell_name = current_command[3]
    if heroes[current_hero_name]["MP"] >= mana_points_needed:
        heroes[current_hero_name]["MP"] -= mana_points_needed
        print(f"{current_hero_name} has successfully cast {spell_name} "
              f"and now has {heroes[current_hero_name]['MP']} MP!")
    else:
        print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")
    return heroes


def taking_damage(heroes, current_command):
    current_hero_name = current_command[1]
    damage = int(current_command[2])
    attacker = current_command[3]
    heroes[current_hero_name]["HP"] -= damage
    if heroes[current_hero_name]["HP"] > 0:
        print(f"{current_hero_name} was hit for {damage} HP by {attacker} "
              f"and now has {heroes[current_hero_name]['HP']} HP left!")
    else:
        print(f"{current_hero_name} has been killed by {attacker}!")
        del heroes[current_hero_name]
    return heroes


def recharge(heroes, current_command):
    current_hero_name = current_command[1]
    amount = int(current_command[2])
    max_mana_points = 200
    amount_recovered = amount
    heroes[current_hero_name]["MP"] += amount
    if heroes[current_hero_name]["MP"] > max_mana_points:
        amount_recovered = amount - (heroes[current_hero_name]["MP"] - max_mana_points)
        heroes[current_hero_name]["MP"] = max_mana_points
    print(f"{current_hero_name} recharged for {amount_recovered} MP!")
    return heroes


def heal(heroes, current_command):
    current_hero_name = current_command[1]
    amount = int(current_command[2])
    max_hit_points = 100
    amount_recovered = amount
    heroes[current_hero_name]["HP"] += amount
    if heroes[current_hero_name]["HP"] > max_hit_points:
        amount_recovered = amount - (heroes[current_hero_name]["HP"] - max_hit_points)
        heroes[current_hero_name]["HP"] = max_hit_points
    print(f"{current_hero_name} healed for {amount_recovered} HP!")
    return heroes


number_of_heroes = int(input())
heroes_dict = dict()

for number in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes_dict[hero_name] = {"HP": int(hit_points), "MP": int(mana_points)}

command = input()
while command != "End":
    new_command = command.split(" - ")
    if new_command[0] == "CastSpell":
        heroes_dict = casting_spell(heroes_dict, new_command)
    elif new_command[0] == "TakeDamage":
        heroes_dict = taking_damage(heroes_dict, new_command)
    elif new_command[0] == "Recharge":
        heroes_dict = recharge(heroes_dict, new_command)
    elif new_command[0] == "Heal":
        heroes_dict = heal(heroes_dict, new_command)
    command = input()
for hero in heroes_dict:
    print(f"{hero}\n  HP: {heroes_dict[hero]['HP']}\n  MP: {heroes_dict[hero]['MP']}")