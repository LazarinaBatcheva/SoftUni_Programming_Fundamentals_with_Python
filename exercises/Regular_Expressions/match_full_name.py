import re

some_names = input()
pattern = r"\b[A-Z][a-z]+[ ]{1}[A-Z][a-z]+\b"
match_names = re.findall(pattern, some_names)
print(" ".join(match_names))