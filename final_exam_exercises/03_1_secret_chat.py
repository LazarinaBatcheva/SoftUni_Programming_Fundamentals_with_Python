def insert_space_in_message(message, index):
    message = message[:index] + " " + message[index:]
    print(message)
    return message


def reverse_string_in_message(message, substring):
    if substring in message:
        message = message.replace(substring, "", 1)
        message = message + substring[::-1]
        print(message)
    else:
        print("error")
    return message


def change_all_substring_in_message(message, substring, replacement):
    if substring in message:
        message = message.replace(substring, replacement)
        print(message)
    return message


def base_function(message):
    command = input()
    while True:
        if command == "Reveal":
            print(f"You have a new text message: {message}")
            break
        instruction, *params = command.split(":|:")
        if instruction == "InsertSpace":
            index = int(params[0])
            message = insert_space_in_message(message, index)
        elif instruction == "Reverse":
            substring = params[0]
            message = reverse_string_in_message(message, substring)
        elif instruction == "ChangeAll":
            substring, replacement = params[0], params[1]
            message = change_all_substring_in_message(message, substring, replacement)
        command = input()


concealed_message = input()
base_function(concealed_message)