integers = [int(x) for x in input().split(", ")]

group = 10
numbers_in_group = []

while integers:
    numbers_in_group = [number for number in integers if number <= group]
    print(f"Group of {group}'s: {numbers_in_group}")
    group += 10
    integers = [number for number in integers if number not in numbers_in_group]