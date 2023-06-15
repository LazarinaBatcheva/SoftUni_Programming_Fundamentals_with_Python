numbers = [int(number) for number in input().split()]

even_numbers = lambda x: x % 2 == 0
result = list(filter(even_numbers, numbers))
print(result)