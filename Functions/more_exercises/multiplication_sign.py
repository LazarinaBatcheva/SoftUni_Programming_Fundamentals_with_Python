def multiplication_sign(num_one, num_two, num_three):
    multiplied_numbers = num_one * num_two * num_three
    if multiplied_numbers > 0:
        return "positive"
    elif multiplied_numbers < 0:
        return "negative"
    else:
        return "zero"


first_number, second_number, third_number = int(input()), int(input()), int(input())

print(multiplication_sign(first_number, second_number, third_number))