numbers_as_string = input().split(', ')

zeros_counter = 0
list_of_numbers = []

for element in numbers_as_string:
    current_number = int(element)
    if current_number == 0:
        zeros_counter += 1
    else:
        list_of_numbers.append(current_number)

for zeros in range(zeros_counter):
    list_of_numbers.append(0)

print(list_of_numbers)
