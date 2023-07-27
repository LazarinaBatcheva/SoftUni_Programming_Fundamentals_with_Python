import re

text = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
match = re.findall(pattern, text)
if match:
    for email in match:
        print(email[0])