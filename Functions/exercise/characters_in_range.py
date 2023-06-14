def found_characters(star_character, end_character):
    characters = []
    for character in range(ord(star_character) + 1, ord(end_character)):
        characters.append(chr(character))
    return characters


first_character = input()
second_character = input()

print(" ".join(found_characters(first_character, second_character)))