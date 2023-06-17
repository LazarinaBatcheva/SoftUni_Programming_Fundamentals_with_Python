first_sequence_of_strings = input().split(", ")
second_sequence_of_strings = input().split(", ")

substrings = []

for first_string in first_sequence_of_strings:
    for second_string in second_sequence_of_strings:
        if first_string in second_string:
            substrings.append(first_string)
            break

print(substrings)