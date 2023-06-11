neighborhood = [int(number) for number in input().split("@")]
command = input()

last_position = 0

while command != "Love!":
    jump_command = command.split()
    jump_index = int(jump_command[1])
    last_position += jump_index

    if last_position >= len(neighborhood):
        last_position = 0

    if neighborhood[last_position] != 0:
        neighborhood[last_position] -= 2
        if neighborhood[last_position] == 0:
            print(f"Place {last_position} has Valentine's day.")
    else:
        print(f"Place {last_position} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {last_position}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    house_count = [1 for house in neighborhood if house != 0]
    print(f"Cupid has failed {sum(house_count)} places.")