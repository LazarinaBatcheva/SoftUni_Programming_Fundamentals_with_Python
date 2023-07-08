some_string = input().upper()

rage_message = ""
current_symbol = ""
repetitions = ""

for index in range(len(some_string)):
    if not some_string[index].isdigit():
        current_symbol += some_string[index]
    else:
        for next_symbol_index in range(index, len(some_string)):
            if not some_string[next_symbol_index].isdigit():
                break
            repetitions += some_string[next_symbol_index]
        rage_message += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)