def found_numbers_count(some_numbers):
    numbers_dict = dict()
    for number in numbers:
        if number not in numbers_dict.keys():
            numbers_dict[number] = 1
        else:
            numbers_dict[number] += 1
    for number, count in sorted(numbers_dict.items()):
        print(f"{number} -> {count}")


numbers = input().split()
found_numbers_count(numbers)