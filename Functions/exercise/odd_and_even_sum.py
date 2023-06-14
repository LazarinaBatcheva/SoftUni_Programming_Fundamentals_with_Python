def odd_even_numbers(numbers):
    sum_of_odd_numbers = 0
    sum_of_even_numbers = 0
    for num in numbers:
        if int(num) % 2 == 0:
            sum_of_even_numbers += int(num)
        else:
            sum_of_odd_numbers += int(num)
    return sum_of_odd_numbers, sum_of_even_numbers


single_number = input()

odd_numbers, even_numbers = odd_even_numbers(single_number)
print(f"Odd sum = {odd_numbers}, Even sum = {even_numbers}")