targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    manipulation_command = command.split()
    index, value = int(manipulation_command[1]), int(manipulation_command[2])

    if "Shoot" in manipulation_command:
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif "Add" in manipulation_command:
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif "Strike" in manipulation_command:
        start_radius = index - value
        end_radius = index + value + 1
        if 0 <= start_radius <= end_radius < len(targets):
            del targets[start_radius:end_radius]
        else:
            print("Strike missed!")

    command = input()

if command == "End":
    print(*targets, sep="|")