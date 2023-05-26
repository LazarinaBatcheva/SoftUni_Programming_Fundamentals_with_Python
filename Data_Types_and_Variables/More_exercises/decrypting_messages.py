key = int(input())
number_of_lines = int(input())

decrypted_message = ''

for i in range(number_of_lines):
    current_letter = input()
    decrypted_current_letter = ord(current_letter) + key
    decrypted_message += chr(decrypted_current_letter)

print(decrypted_message)