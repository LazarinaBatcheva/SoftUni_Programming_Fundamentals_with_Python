list_of_integers = input().split()
count_of_numbers_to_remove = int(input())

remaining_numbers = []
removed_numbers_counter = 0

for element in list_of_integers:
    current_number = int(element)
    remaining_numbers.append(current_number)

while removed_numbers_counter < count_of_numbers_to_remove:
    min_number = min(remaining_numbers)
    remaining_numbers.remove(min_number)
    removed_numbers_counter += 1

list_of_integers = remaining_numbers

remaining_numbers_as_strings = []

for number in remaining_numbers:
    current_number_as_string = str(number)
    remaining_numbers_as_strings.append(current_number_as_string)

print(', '.join(remaining_numbers_as_strings))
