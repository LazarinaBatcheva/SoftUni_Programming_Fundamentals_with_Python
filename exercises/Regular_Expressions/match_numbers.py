import re

numbers = input()
pattern = r"(^|(?<=\s))-?(\d*)(\.\d+)?($|(?=\s))"
match = re.finditer(pattern, numbers)
if match:
    for number in match:
        print(number[0], end=" ")