def merge(strings_list, start_i, end_i):
    if start_i < 0:
        start_i = 0
    if end_i > len(strings_list) - 1:
        end_i = len(strings_list) - 1
    elements_for_merge = strings_list[start_i:end_i + 1]
    new_word = ""
    for element in elements_for_merge:
        new_word += element
        strings_list.remove(element)
    strings_list.insert(start_i, new_word)
    return strings_list


def divide(strings_list, index, partition):
    word_for_divide = strings_list.pop(index)
    if len(word_for_divide) >= partition:
        word_parts_length = len(word_for_divide) // partition
        word_parts_list = []
        for _ in range(partition - 1):
            word_parts_list.append(word_for_divide[:word_parts_length])
            word_for_divide = word_for_divide[word_parts_length:]
        word_parts_list.append(word_for_divide)
        for element in word_parts_list[::-1]:
            strings_list.insert(index, element)
    return strings_list


some_strings = [word for word in input().split()]
command = input()

while command != "3:1":
    command = command.split()
    action, start_index, end_index = command[0], int(command[1]), int(command[2])

    if action == "merge":
        merge(some_strings, start_index, end_index)

    elif action == "divide":
        divide(some_strings, start_index, end_index)

    command = input()

print(*some_strings)
