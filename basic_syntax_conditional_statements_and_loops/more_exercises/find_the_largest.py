number_input = input()

largest_number = list(number_input)
largest_number.sort(reverse=True)
for i in largest_number:
    print(i, end='')