sequence_of_words = input().lower().split()
words_dict = {}
odd_words_list = []

for word in sequence_of_words:
    if word not in words_dict.keys():
        words_dict[word] = 0
    words_dict[word] += 1

for word in words_dict:
    if words_dict[word] % 2 != 0:
        odd_words_list.append(word)

print(", ".join(map(str, odd_words_list)))