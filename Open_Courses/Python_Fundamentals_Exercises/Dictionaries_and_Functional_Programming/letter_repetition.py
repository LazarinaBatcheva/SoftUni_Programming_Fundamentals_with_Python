some_string = input()
characters_info_dict = {}

for character in some_string:
    if character not in characters_info_dict.keys():
        characters_info_dict[character] = 0
    characters_info_dict[character] += 1

for key, value in characters_info_dict.items():
    print(f"{key} -> {value}")