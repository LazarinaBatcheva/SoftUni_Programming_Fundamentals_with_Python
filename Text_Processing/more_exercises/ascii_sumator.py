def ascii_sum(first_ch, last_ch, text):
    total_sum = 0
    for character in text:
        if ord(character) in range(ord(first_ch) + 1, ord(last_ch)):
            total_sum += ord(character)
    return total_sum


start_character = input()
end_character = input()
some_string = input()

print(ascii_sum(start_character, end_character, some_string))