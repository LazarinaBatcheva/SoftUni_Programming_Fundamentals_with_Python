def factorial_of_numbers(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())

first_number_factorial = factorial_of_numbers(first_number)
second_number_factorial = factorial_of_numbers(second_number)
numbers_division = first_number_factorial / second_number_factorial

print(f"{numbers_division:.2f}")
