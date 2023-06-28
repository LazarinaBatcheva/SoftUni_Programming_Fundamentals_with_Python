hidden_message = input()

characters_list = [character for character in hidden_message if not character.isdigit()]
numbers_list = [int(character) for character in hidden_message if character.isdigit()]
final_string = []

while numbers_list:
    take_letters, skip_letters = numbers_list.pop(0), numbers_list.pop(0)
    final_string += characters_list[:take_letters]
    characters_list = characters_list[take_letters + skip_letters:]

print("".join(final_string))