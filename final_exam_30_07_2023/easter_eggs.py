import re

text_string = input()
pattern = r"[#@]+([a-z]{3,})[#@]+[^A-Za-z\d]*[/]+(\d+)[/]+"
matches = re.findall(pattern, text_string)
if matches:
    for color, amount in matches:
        print(f"You found {amount} {color} eggs!")