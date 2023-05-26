import string

some_text = input()

capital_letter = string.ascii_uppercase
letter_position = list()
position = 0

for letter in some_text:
    if letter in capital_letter:
        letter_position.append(position)
    position += 1

print(letter_position)

# word = input()
# list_to_print = []
# for el in range(len(word)):
#     if word[el].isalpha() and word[el].isupper():
#         list_to_print.append(el)
# print(list_to_print)