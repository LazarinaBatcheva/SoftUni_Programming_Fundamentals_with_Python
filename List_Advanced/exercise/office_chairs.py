def chairs(rooms):
    free_chairs = 0
    for room in range(1, rooms + 1):
        information = input().split()
        number_of_chairs, visitors = information[0], int(information[1])
        difference = len(number_of_chairs) - visitors
        if difference >= 0:
            free_chairs += difference
        else:
            print(f"{visitors - len(number_of_chairs)} more chairs needed in room {room}")
            free_chairs += difference
    return free_chairs


number_of_rooms = int(input())
total_free_chairs = chairs(number_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")