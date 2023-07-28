import re

string = input()
pattern = r"\b[0-9A-F]+\b|\b0x[0-9A-F]+\b"
hexadecimal_numbers = re.findall(pattern, string)
if hexadecimal_numbers:
    print(" ".join(hexadecimal_numbers))