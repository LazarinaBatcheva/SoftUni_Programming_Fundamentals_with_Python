wagons = [0] * int(input())
command = input()

while command != "End":
    command = command.split()
    action = command[0]

    if action == "add":
        people = int(command[1])
        wagons[-1] += people

    elif action == "insert":
        index, people = int(command[1]), int(command[2])
        wagons[index] += people

    elif action == "leave":
        index, people = int(command[1]), int(command[2])
        wagons[index] -= people

    command = input()

print(wagons)