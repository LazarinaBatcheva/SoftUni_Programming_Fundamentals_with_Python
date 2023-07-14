import re

sentence = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
variable_names = re.findall(pattern, sentence)
print(",".join(variable_names))