divisor, boundary = int(input()), int(input())

largest_number = 0

for i in range(boundary, divisor - 1, -1):
    if i % divisor == 0:
        largest_number += i
        print(f"{largest_number}")
        break