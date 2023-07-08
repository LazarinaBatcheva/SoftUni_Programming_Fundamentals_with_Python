some_string = input().split()
final_string = ""
for word in some_string:
    final_string += word * len(word)
print(final_string)