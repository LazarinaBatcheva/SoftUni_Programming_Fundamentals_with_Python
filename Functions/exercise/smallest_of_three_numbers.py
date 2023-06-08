def the_smallest_number(numbers):
    min_number = min(numbers)
    return min_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

numbers_list = [first_number, second_number, third_number]
the_smallest_element = the_smallest_number(numbers_list)

print(the_smallest_element)