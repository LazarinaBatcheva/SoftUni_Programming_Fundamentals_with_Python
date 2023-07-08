string_for_remove = input()
text = input()
while string_for_remove in text:
    text = text.replace(string_for_remove, "")
print(text)