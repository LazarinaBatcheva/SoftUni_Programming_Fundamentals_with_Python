def replace_letters_with_uppercase(text):
    text = text.upper()
    print(text)
    return text


def replace_letters_with_lowercase(text):
    text = text.lower()
    print(text)
    return text


def replace_letter(action, text):
    index = int(action[1])
    letter = action[2]
    if 0 <= index < len(text):
        text = text[:index] + letter + text[index + 1:]
        print("Done!")
    else:
        print("The spell was too weak.")
    return text


def replace_substring(action, text):
    first_string = action[1]
    second_string = action[2]
    if first_string in text:
        text = text.replace(first_string, second_string)
        print(text)
    return text


def remove_substring(action, text):
    substring = action[1]
    if substring in text:
        text = text.replace(substring, "", 1)
        print(text)
    return text


some_string = input()
command = input()
while command != "Abracadabra":
    current_command = command.split()
    if current_command[0] == "Abjuration":
        some_string = replace_letters_with_uppercase(some_string)
    elif current_command[0] == "Necromancy":
        some_string = replace_letters_with_lowercase(some_string)
    elif current_command[0] == "Illusion":
        some_string = replace_letter(current_command, some_string)
    elif current_command[0] == "Divination":
        some_string = replace_substring(current_command, some_string)
    elif current_command[0] == "Alteration":
        some_string = remove_substring(current_command, some_string)
    else:
        print("The spell did not work!")
    command = input()