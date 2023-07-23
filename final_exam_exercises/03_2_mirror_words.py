import re


def found_match_words(matches, words_list):
    for match in matches:
        if match["word1"] == match["word2"][::-1]:
            words_list.append(f"{match['word1']} <=> {match['word2']}")
    if words_list:
        print("The mirror words are:")
        print(", ".join(words_list))
    else:
        print("No mirror words!")


def base_function(text):
    words_list = list()
    pattern = re.compile(r"([@#])(?P<word1>[a-zA-Z]{3,})\1\1(?P<word2>[a-zA-Z]{3,})\1")
    matches = list(re.finditer(pattern, text))
    if matches:
        print(f"{len(matches)} word pairs found!")
    else:
        print("No word pairs found!")
    found_match_words(matches, words_list)


text_string = input()
base_function(text_string)