numbers = [int(num) for num in input().split()]
control_number = int(input())

new_numbers_list = []

for number in sorted(numbers, reverse=True):
    new_numbers_list.append(number)
    if len(new_numbers_list) == control_number:
        break

print(' '.join(map(str, new_numbers_list)))