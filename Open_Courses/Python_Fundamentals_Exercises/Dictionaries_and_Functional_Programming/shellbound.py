from math import ceil

def add_shells(region, shells, shells_info_dict):
    if region not in shells_info_dict.keys():
        shells_info_dict[region] = []
    if shells not in shells_info_dict[region]:
        shells_info_dict[region].append(shells)
    return shells_info_dict


def show_results(shells_info_dict):
    for region in shells_info_dict.keys():
        giant_shell = (sum(shells_info_dict[region]) -
                       (sum(shells_info_dict[region]) / len(shells_info_dict[region])))
        print(f"{region} -> ", end="")
        print(", ".join(map(str, shells_info_dict[region])), end="")
        print(f" ({ceil(giant_shell)})")


def base_function(current_command):
    shells_info_dict = {}
    while current_command != "Aggregate":
        current_command = current_command.split()
        region, shells = current_command[0], int(current_command[1])
        shells_info_dict = add_shells(region, shells, shells_info_dict)
        current_command = input()
    show_results(shells_info_dict)


command = input()
base_function(command)