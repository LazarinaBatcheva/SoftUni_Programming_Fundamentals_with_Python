def battlefield(rows):
    for row in range(rows):
        row = [int(number) for number in input().split()]
        battlefield_list.append(row)


def attack_ship(positions):
    destroyed_ships = 0
    for attack in positions:
        row, col = [int(number) for number in attack.split("-")]
        battlefield_list[row][col] -= 1
        if battlefield_list[row][col] == 0:
            destroyed_ships += 1
    return destroyed_ships


number_of_row = int(input())
battlefield_list = []

battlefield(number_of_row)

attacks = input().split()

print(attack_ship(attacks))
