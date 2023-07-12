def move_letters(current_message, number_of_letters):
    return current_message[number_of_letters:] + current_message[:number_of_letters]


def insert_characters(current_message, index, value):
    return current_message[:index] + value + current_message[index:]
    pass


def change_all_characters(current_message, character_for_replace, new_character):
    return current_message.replace(character_for_replace, new_character)


message = input()
command = input()

while command != "Decode":
    current_command = command.split("|")
    if current_command[0] == "Move":
        letters = int(current_command[1])
        message = move_letters(message, letters)
    elif current_command[0] == "Insert":
        insert_index, insert_value = int(current_command[1]), current_command[2]
        message = insert_characters(message, insert_index, insert_value)
    elif current_command[0] == "ChangeAll":
        substring, replacement = current_command[1], current_command[2]
        message = change_all_characters(message, substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")