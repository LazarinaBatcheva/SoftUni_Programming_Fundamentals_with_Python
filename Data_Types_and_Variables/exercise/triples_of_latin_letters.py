number = int(input())

for first_letter in range(number):
    for second_letter in range(number):
        for third_letter in range(number):

            print(f'{chr(97 + first_letter)}'
                  f'{chr(97 + second_letter)}'
                  f'{chr(97 + third_letter)}')