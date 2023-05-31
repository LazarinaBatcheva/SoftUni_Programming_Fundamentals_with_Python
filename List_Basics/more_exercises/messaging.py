sequence_of_numbers = input().split()
some_text = input()

message = ""
some_text_list = [character for character in some_text]

for numbers in sequence_of_numbers:
    find_index = sum(int(current_number) for current_number in numbers)
    if find_index >= len(some_text_list):
        find_index -= len(some_text_list)
    message += some_text_list[find_index]
    del some_text_list[find_index]

print(message)