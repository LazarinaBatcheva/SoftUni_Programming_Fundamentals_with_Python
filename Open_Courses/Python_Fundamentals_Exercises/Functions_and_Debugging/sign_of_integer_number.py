def check_for_number(some_number):
    if some_number > 0:
        return f"The number {some_number} is positive."
    elif some_number < 0:
        return f"The number {some_number} is negative."
    else:
        return f"The number {some_number} is zero."


number = int(input())
print(check_for_number(number))