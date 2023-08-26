numbers = input().split()
numbers_dict = {}

for number in numbers:
    number = float(number)
    if number not in numbers_dict.keys():
        numbers_dict[number] = 0
    numbers_dict[number] += 1

for key, value in sorted(numbers_dict.items()):
    print(f"{key} -> {value} times")