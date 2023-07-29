def replace_character(text, current_command):
    current_character = current_command[1]
    new_character = current_command[2]
    if current_character in text:
        text = text.replace(current_character, new_character)
        print(text)
    return text


def cut_substring(text, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    if start_index < 0 or end_index >= len(text):
        print("Invalid indexes!")
    else:
        text = text[:start_index] + text[end_index + 1:]
        print(text)
    return text


def make_upper_lower_letters(text, current_command):
    upper_lower = current_command[1]
    if upper_lower == "Upper":
        text = text.upper()
    else:
        text = text.lower()
    print(text)
    return text


def check_string(text, current_command):
    string = current_command[1]
    if string in text:
        print(f"Message contains {string}")
    else:
        print(f"Message doesn't contain {string}")


def sum_substring(text, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    if start_index < 0 or end_index >= len(text):
        print("Invalid indexes!")
    else:
        substring = text[start_index:end_index + 1]
        substring_sum = sum(ord(character) for character in substring)
        print(substring_sum)


def base_function(text, current_command):
    while current_command != "Finish":
        current_command = current_command.split()
        if current_command[0] == "Replace":
            text = replace_character(text, current_command)
        elif current_command[0] == "Cut":
            text = cut_substring(text, current_command)
        elif current_command[0] == "Make":
            text = make_upper_lower_letters(text, current_command)
        elif current_command[0] == "Check":
            check_string(text, current_command)
        elif current_command[0] == "Sum":
            sum_substring(text, current_command)
        current_command = input()


some_string = input()
command = input()
base_function(some_string, command)