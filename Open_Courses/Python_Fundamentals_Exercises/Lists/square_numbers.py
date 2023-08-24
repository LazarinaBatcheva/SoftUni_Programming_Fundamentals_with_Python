import math

integers_list = [int(number) for number in input().split()]
square_numbers_list = []

for number in integers_list:
    if number > 0:
        sgr_number = math.sqrt(number)
        if sgr_number.is_integer():
            square_numbers_list.append(number)

square_numbers_list.sort(reverse=True)
print(" ".join(map(str,square_numbers_list)))
