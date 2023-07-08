some_strings = input().split()

total_sum = 0

for current_string in some_strings:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    current_number = int(current_string[1:len(current_string) - 1])
    if first_letter.isupper():
        total_sum += current_number / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum += current_number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total_sum -= ord(last_letter) - 64
    elif last_letter.islower():
        total_sum += ord(last_letter) - 96

print(f"{total_sum:.2f}")