word = input()
sentence = input()
if word in sentence:
    sentence = sentence.replace(word, "*" * len(word))
print(sentence)