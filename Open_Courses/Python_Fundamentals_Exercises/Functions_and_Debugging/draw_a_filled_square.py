def create_figure(number):
    characters = "\/"
    figure = f"-{(number - 1) * characters}-"
    for num in range(1, number - 1):
        print(figure)


def base_function(number):
    first_last_line = "-" * number * 2
    print(first_last_line)
    create_figure(number)
    print(first_last_line)


number_of_lines = int(input())
base_function(number_of_lines)