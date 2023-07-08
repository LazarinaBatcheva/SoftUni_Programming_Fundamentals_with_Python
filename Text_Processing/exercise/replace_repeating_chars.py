some_string = input()
final_string = ""
last_letter = ""
for letter in some_string:
    if letter != last_letter:
        final_string += letter
        last_letter = letter
print(final_string)