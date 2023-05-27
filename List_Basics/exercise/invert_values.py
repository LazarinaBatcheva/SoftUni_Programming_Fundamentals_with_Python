numbers_list = input().split()

inverted_values_of_numbers = []

for element in numbers_list:
    current_number = -int(element)
    inverted_values_of_numbers.append(current_number)

print(inverted_values_of_numbers)