def containing_string(text, current_command):
    substring = current_command[1]
    if substring in text:
        print(f"{text} contains {substring}")
    else:
        print("Substring not found!")


def flipping(text, current_command):
    upper_lower = current_command[1]
    start_index = int(current_command[2])
    end_index = int(current_command[3])
    substring = text[start_index: end_index]
    if upper_lower == "Upper":
        substring = substring.upper()
    elif upper_lower == "Lower":
        substring = substring.lower()
    text = text[:start_index] + substring + text[end_index:]
    print(text)
    return text


def slicing(text, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    text = text[:start_index] + text[end_index:]
    print(text)
    return text


activation_key = input()
command = input()

while command != "Generate":
    new_command = command.split(">>>")
    if new_command[0] == "Contains":
        containing_string(activation_key, new_command)
    elif new_command[0] == "Flip":
        activation_key = flipping(activation_key, new_command)
    elif new_command[0] == "Slice":
        activation_key = slicing(activation_key, new_command)
    command = input()
print(f"Your activation key is: {activation_key}")