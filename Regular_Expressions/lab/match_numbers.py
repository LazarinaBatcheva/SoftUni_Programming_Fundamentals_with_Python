import re

numbers = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9]\d*)(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, numbers)
for match in matches:
    print(match[0], end=" ")