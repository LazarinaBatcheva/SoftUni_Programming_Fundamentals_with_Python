number_of_lines = int(input())
word = input()

list_of_strings = []
filtered_list_of_strings = []

for i in range(number_of_lines):
    string = input()
    list_of_strings.append(string)
    if word in string:
        filtered_list_of_strings.append(string)

print(list_of_strings)
print(filtered_list_of_strings)