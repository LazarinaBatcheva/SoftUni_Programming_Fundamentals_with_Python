sequence_of_words = input().lower().split()
words_dict = {}
for word in sequence_of_words:
    word_count = sequence_of_words.count(word)
    if word_count % 2 != 0:
        words_dict[word] = word_count
print(*words_dict, sep=", ")