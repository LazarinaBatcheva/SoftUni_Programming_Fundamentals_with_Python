morse_code_letters = input().split("|")
message = ""

for letter in morse_code_letters:
    total_sum = 0
    current_digit = letter[0]
    current_count = 1
    
    for index in range(1, len(letter)):
        if letter[index] == current_digit:
            current_count += 1
            
        elif letter[index] != current_digit:
            total_sum += current_count * (3 if current_digit == '0' else 5)
            current_digit = letter[index]
            if current_count > 1:
                total_sum += current_count
            current_count = 1
            
        if index == (len(letter) - 1):
            total_sum += current_count * (3 if current_digit == '0' else 5)
            current_digit = letter[index]
            if current_count > 1:
                total_sum += current_count
                
    message += chr(total_sum)
print(message)
