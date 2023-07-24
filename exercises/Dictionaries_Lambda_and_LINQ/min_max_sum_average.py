number_of_lines = int(input())
numbers_list = [int(input()) for number in range(number_of_lines)]
print(f"Sum = {sum(numbers_list)}")
print(f"Min = {min(numbers_list)}")
print(f"Max = {max(numbers_list)}")
print(f"Average = {sum(numbers_list) / len(numbers_list)}")



# number_of_lines = int(input())
# numbers_list = []
# for number in range(number_of_lines):
#     current_number = int(input())
#     numbers_list.append(current_number)
# print(f"Sum = {sum(numbers_list)}")
# print(f"Min = {min(numbers_list)}")
# print(f"Max = {max(numbers_list)}")
# print(f"Average = {sum(numbers_list) / len(numbers_list)}")
