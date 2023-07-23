def add_destination(index, current_stop, stops):
    if 0 <= index < len(stops):
        stops = stops[:index] + current_stop + stops[index:]
    return stops


def remove_destination(start_index, end_index, stops):
    if start_index <= end_index and end_index < len(stops):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch_destination(old_stop, new_stop, stops):
    if old_stop in stops:
        stops = stops.replace(old_stop, new_stop)
    return stops


destinations = input()
command = input()

while command != "Travel":
    command = command.split(":")
    if "Add Stop" in command:
        stop_index, destination = int(command[1]), command[2]
        destinations = add_destination(stop_index, destination, destinations)
    elif "Remove Stop" in command:
        first_index, last_index = int(command[1]), int(command[2])
        destinations = remove_destination(first_index, last_index, destinations)
    elif "Switch" in command:
        old_destination, new_destination = command[1], command[2]
        destinations = switch_destination(old_destination, new_destination, destinations)
    command = input()
    print(destinations)

if command == "Travel":
    print(f"Ready for world tour! Planned stops: {destinations}")