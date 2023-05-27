factor = int(input())
count = int(input())

list_of_numbers = []

for number in range(1, count + 1):
    current_number = factor * number
    list_of_numbers.append(current_number)

print(list_of_numbers)