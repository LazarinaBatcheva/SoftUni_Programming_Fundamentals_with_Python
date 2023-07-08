corresponding_numbers = [int(number) for number in input().split()]
text = input()

decrypted_message = ""
type_of_treasure = ""
coordinates = ""

while text != "find":
    while text:
        current_text = text[:len(corresponding_numbers)]
        for index in range(len(current_text)):
            decrypted_message += chr(ord(current_text[index]) - corresponding_numbers[index])
        text = text[len(corresponding_numbers):]

    # found type of treasure
    start_index = decrypted_message.find("&") + 1
    end_index = decrypted_message.find("&", start_index)
    type_of_treasure = decrypted_message[start_index:end_index]
    coordinates = decrypted_message[decrypted_message.index("<") + 1:decrypted_message.index(">")]
    print(f"Found {type_of_treasure} at {coordinates}")

    decrypted_message = ""
    type_of_treasure = ""
    coordinates = ""
    text = input()