quantity_of_decorations = int(input())
days_left_until_Christmas = int(input())

ORNAMENT_SET_PRICE = 2
TREE_SKIRT = 5
TREE_GARLAND = 3
TREE_LIGHTS = 15

total_cost = 0
total_spirit = 0

for day in range(1, days_left_until_Christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += ORNAMENT_SET_PRICE * quantity_of_decorations
        total_spirit += 5
    if day % 3 == 0:
        total_cost += (TREE_SKIRT + TREE_GARLAND) * quantity_of_decorations
        total_spirit += 13
    if day % 5 == 0:
        total_cost += TREE_LIGHTS * quantity_of_decorations
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += TREE_SKIRT + TREE_GARLAND + TREE_LIGHTS

if days_left_until_Christmas % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}\nTotal spirit: {total_spirit}')