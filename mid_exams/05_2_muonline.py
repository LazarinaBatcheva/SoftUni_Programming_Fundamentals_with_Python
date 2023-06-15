dungeons_rooms = input().split("|")

health = 100
bitcoins = 0
best_room = 0
is_dead = False

for room in dungeons_rooms:
    command, number = room.split()
    amount = int(number)
    best_room += 1

    if command == "potion":
        if health + amount > 100:
            amount = 100 - health
        health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else: #command == monster
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            is_dead = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")