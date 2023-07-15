import re

all_names = input()
command = input()
racers = dict()

pattern_names = re.compile(r"([A-Za-z])")
pattern_numbers = re.compile(r"([0-9])")

while command != "end of race":
    found_name = "".join(re.findall(pattern_names, command))
    if found_name in all_names:
        found_numbers = sum(int(num) for num in re.findall(pattern_numbers, command))
        if found_name not in racers:
            racers[found_name] = racers.get(found_name, 0)
        racers[found_name] += found_numbers
    command = input()

racers = sorted(racers.items(), key=lambda x: -x[1])
print(f"1st place: {racers[0][0]}")
print(f"2nd place: {racers[1][0]}")
print(f"3rd place: {racers[2][0]}")
