numbers_list = [float(number) for number in input().split()]

is_match = True
while is_match:
    is_match = False
    for index, number in enumerate(numbers_list, 1):
        if index < len(numbers_list) and number == numbers_list[index]:
            numbers_list[index-1] = number + numbers_list[index]
            numbers_list.pop(index)
            is_match = True
            break

print(" ".join(map(str, numbers_list)))