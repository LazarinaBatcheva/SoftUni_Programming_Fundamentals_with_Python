def check_for_palindromes(numbers):
    if number == number[::-1]:
        return True
    return False


integers = input().split(", ")

for number in integers:
    print(check_for_palindromes(integers))