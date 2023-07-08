command = input()
contests = dict()
individual_info = dict()

while command != "no more time":
    name, contest, points = [int(x) if x.isdigit() else x for x in command.split(" -> ")]
    contests[contest] = contests.get(contest, {})
    contests[contest][name] = contests[contest].get(name, 0)
    if contests[contest][name] < points:
        contests[contest][name] = points
    command = input()

position = 1
for contest in contests:
    print(f"{contest}: {len(contests[contest])} participants")
    for name, points in sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])):
        print(f"{position}. {name} <::> {points}")
        position += 1
        individual_info[name] = individual_info.get(name, 0) + points
    position = 1

print("Individual standings:")
for name, points in sorted(individual_info.items(), key=lambda x: (-x[1], x[0])):
    print(f"{position}. {name} -> {points}")
    position += 1