number_of_integers = int(input())
numbers_list = []

for i in range(number_of_integers):
    current_number = int(input())
    numbers_list.append(current_number)

print(sum(numbers_list))