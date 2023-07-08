text = input()
encrypted_text = ""
for character in text:
    encrypted_text += chr(ord(character) + 3)
print(encrypted_text)