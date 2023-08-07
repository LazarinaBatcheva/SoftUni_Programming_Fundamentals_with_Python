def base_function(numbers_list):
    even_numbers = []
    odd_numbers = []
    for ch in numbers_list:
        if ch == "-":
            continue
        else:
            number = int(ch)
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
    return sum(even_numbers) * sum(odd_numbers)


sequence_of_numbers = input()
print(base_function(sequence_of_numbers))