import re

some_string = input()
while some_string:
    pattern = r"\d+"
    found_numbers = re.findall(pattern, some_string)
    if found_numbers:
        print(" ".join(found_numbers), end=" ")
    some_string = input()