integers_list = [int(number) for number in input().split()]
odd_numbers_list = []

for number in integers_list:
    if number % 2 != 0:
        odd_numbers_list.append(number)

print(len(odd_numbers_list))