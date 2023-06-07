operator_as_string = input()
first_number = int(input())
second_number = int(input())


def outcome(operator, num1, num2):
    result = None
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 // num2
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    return result


print(outcome(operator_as_string, first_number, second_number))