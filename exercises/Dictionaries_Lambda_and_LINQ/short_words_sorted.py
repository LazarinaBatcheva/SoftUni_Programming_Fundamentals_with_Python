input_text = input().lower()
words = input_text.split()
words_set = set()
for word in words:
    word = word.strip(".,:;()[]\'/!?\"")
    if len(word) < 5:
        words_set.add(word)
print(", ".join(sorted(words_set)))