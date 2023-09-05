list_of_integers = [int(num) for num in input().split()]
numbers_dict = {}

for number in list_of_integers:
    if number not in numbers_dict.keys():
        numbers_dict[number] = 1
    else:
        numbers_dict[number] += 1

for num, count in sorted(numbers_dict.items()):
    print(f"{num} -> {count}")