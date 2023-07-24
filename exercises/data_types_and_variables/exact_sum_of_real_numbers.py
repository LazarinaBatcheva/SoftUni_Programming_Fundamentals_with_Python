from decimal import Decimal

number_of_lines = int(input())
exact_sum = 0
for _ in range(number_of_lines):
    current_number = Decimal(input())
    exact_sum += current_number
print(exact_sum)