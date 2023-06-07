sequence_of_numbers = input().split()

absolute_numbers_list = [abs(float(number)) for number in sequence_of_numbers]
print(absolute_numbers_list)