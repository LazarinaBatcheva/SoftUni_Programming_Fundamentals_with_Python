some_string = input()
digits = ""
letters = ""
characters = ""
for character in some_string:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        characters += character
print(digits)
print(letters)
print(characters)