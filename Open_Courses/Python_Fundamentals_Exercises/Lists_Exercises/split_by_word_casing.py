separators = (",", ";", ":", ".", "!", "(", ")", "\"", "'", "\\", "/", "[", "]", " ")

text = input()

for ch in separators:
    text = text.replace(ch, " ")

lower_case = []
mixed_case = []
upper_case = []

for word in text.split():
    if word.islower() and word.isalpha():
        lower_case.append(word)
    elif word.isupper() and word.isalpha():
        upper_case.append(word)
    else:
        mixed_case.append(word)

print("Lower-case: " + ', '.join(lower_case))
print("Mixed-case: " + ', '.join(mixed_case))
print("Upper-case: " + ', '.join(upper_case))