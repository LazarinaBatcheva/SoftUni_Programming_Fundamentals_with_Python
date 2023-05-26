start_char_index = int(input())
last_char_index = int(input())

for number in range(start_char_index, last_char_index + 1):
    character = chr(number)

    print(f'{character}', end=' ')