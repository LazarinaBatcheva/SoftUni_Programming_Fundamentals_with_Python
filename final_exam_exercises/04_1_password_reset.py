def take_odd_indices(text):
    new_text = ""
    for index in range(len(text)):
        if index % 2 != 0:
            new_text += text[index]
    print(new_text)
    return new_text


def cutting_text(text, current_command):
    index, length = int(current_command[1]), int(current_command[2])
    text = text[:index] + text[index + length:]
    print(text)
    return text


def text_replacement(text, current_command):
    substring, substitute = current_command[1], current_command[2]
    if substring in text:
        text = text.replace(substring, substitute)
        print(text)
    else:
        print("Nothing to replace!")
    return text


password = input()
command = input()

while command != "Done":
    if command == "TakeOdd":
        password = take_odd_indices(password)
    new_command = command.split()
    if new_command[0] == "Cut":
        password = cutting_text(password, new_command)
    elif new_command[0] == "Substitute":
        password = text_replacement(password, new_command)
    command = input()
print(f"Your password is: {password}")