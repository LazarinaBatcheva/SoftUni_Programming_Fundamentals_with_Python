words = [word for word in input().lower().split()]

dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")