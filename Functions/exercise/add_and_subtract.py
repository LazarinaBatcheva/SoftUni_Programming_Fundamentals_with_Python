def sum_numbers(first_number, second_number):
    return first_number + second_number

def subtract(sum, third_number):
    return sum - third_number

def add_and_subtract(first_number, second_number, third_number):
    sum_of_the_first_two_numbers = sum_numbers(first_number, second_number)
    result = subtract(sum_of_the_first_two_numbers, third_number)
    return result


number_one, number_two, number_tree = int(input()), int(input()), int(input())

print(add_and_subtract(number_one, number_two, number_tree))