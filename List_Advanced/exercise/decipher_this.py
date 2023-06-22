def deciphered_message(some_message):
    words, numbers = [], []
    number, letter = "", ""
    for character in some_message:
        if character.isdigit():
            number += character
        else:
            letter += character
    numbers.append(int(number))
    first_letter = chr(numbers[0])

    if len(letter) > 0:
        current_letter = [let for let in letter]
        current_letter[0], current_letter[-1] = current_letter[-1], current_letter[0]
        words.append(current_letter)
    return first_letter + "".join(current_letter)


message = input().split()

for i in range(len(message)):
    message[i] = deciphered_message(str(message[i]))
print(*message)
