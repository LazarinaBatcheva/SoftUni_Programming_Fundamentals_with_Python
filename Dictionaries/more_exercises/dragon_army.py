def add_dragons_stats(color, name, damage, health, armor):
    categorized_dragons[color] = categorized_dragons.get(color, {})
    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)
    categorized_dragons[color][name] = damage, health, armor


def calculate_result():
    for color in categorized_dragons.keys():
        damage, health, armor, dragons_count = 0, 0, 0, 0
        for key, value in sorted(categorized_dragons[color].items()):
            damage += value[0]
            health += value[1]
            armor += value[2]
            dragons_count = len(categorized_dragons[color])
        print(f"{color}::({damage / dragons_count:.2f}/{health / dragons_count:.2f}/{armor / dragons_count:.2f})")
        for key, value in sorted(categorized_dragons[color].items()):
            print(f"-{key} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}")


number_of_dragons = int(input())
categorized_dragons = dict()

for number in range(number_of_dragons):
    dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor = input().split()
    add_dragons_stats(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)
calculate_result()