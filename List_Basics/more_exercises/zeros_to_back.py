numbers_as_string = input().split(', ')

zeroes_counter = 0
list_of_numbers = []

for element in numbers_as_string:
    current_number = int(element)
    if current_number == 0:
        zeroes_counter += 1
    else:
        list_of_numbers.append(current_number)

for zeroes in range(zeroes_counter):
    list_of_numbers.append(0)

print(list_of_numbers)