def add_dwarfs(name, hat_color, physics):
    if hat_color not in dwarfs_store.keys():
        dwarfs_store[hat_color] = {}
    if name not in dwarfs_store[hat_color].keys():
        dwarfs_store[hat_color][name] = physics
    else:
        if dwarfs_store[hat_color][name] < physics:
            dwarfs_store[hat_color][name] = physics


command = input()

dwarfs_store = dict()

while command != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = [int(x) if x.isdigit() else x for x in command.split(" <:> ")]
    add_dwarfs(dwarf_name, dwarf_hat_color, dwarf_physics)

    command = input()

dwarfs_list = []
for color, dwarf in dwarfs_store.items():
    for dwarf_name, physic in dwarf.items():
        dwarfs_list.append({"name": dwarf_name, "physic": physic, "hat": color, "dwarfs_count": len(dwarf)})

for dwarf in sorted(dwarfs_list, key=lambda x: (-x["physic"], -x["dwarfs_count"])):
    print(f"({dwarf['hat']}) {dwarf['name']} <-> {dwarf['physic']}")