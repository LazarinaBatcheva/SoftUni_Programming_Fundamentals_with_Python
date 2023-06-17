words = input().split()
palindrome_word = input()

palindrome_words_list = []

for word in words:
    if word == word[::-1]:
        palindrome_words_list.append(word)

palindrome_counter = palindrome_words_list.count(palindrome_word)

print(palindrome_words_list)
print(f"Found palindrome {palindrome_counter} times")


# def palindrome_words(word):
#     if word == word[::-1]:
#         return word


# words = input().split()
# palindrome_word = input()

# palindrome_words_list = [word for word in words if palindrome_words(word)]
# palindrome_counter = palindrome_words_list.count(palindrome_word)

# print(palindrome_words_list)
# print(f"Found palindrome {palindrome_counter} times")
