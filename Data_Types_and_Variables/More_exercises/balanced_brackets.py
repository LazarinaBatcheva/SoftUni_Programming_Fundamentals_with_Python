number_of_lines = int(input())

current_bracket = ''
opening_brackets = 0
closing_brackets = 0
balanced = True

for i in range(number_of_lines):
    character = input()
    if character == '(':
        current_bracket = '('
        opening_brackets += 1
    if character == ')':
        closing_brackets += 1
        if current_bracket != '(':
            balanced = False
            break
        else:
            current_bracket = ')'

if balanced and opening_brackets == closing_brackets:
    print('BALANCED')
else:
    print('UNBALANCED')