import re


def found_cool_threshold(text_string):
    threshold = re.findall(r"\d", text_string)
    cool_threshold_sum = 1
    for number in threshold:
        cool_threshold_sum *= int(number)
    print(f"Cool threshold: {cool_threshold_sum}")
    return cool_threshold_sum


def found_emojis(text_string, cool_threshold_sum):
    pattern = re.compile(r"(:{2})(?P<emoji1>[A-Z][a-z]{2,})(::)|"
                         r"(\*\*)(?P<emoji2>[A-Z][a-z]{2,})(\*{2})")
    emojis = list(re.finditer(pattern, text_string))
    print(f"{len(emojis)} emojis found in the text. The cool ones are:")
    for emoji in emojis:
        if emoji["emoji1"]:
            cool_emoji = emoji["emoji1"]
        elif emoji["emoji2"]:
            cool_emoji = emoji["emoji2"]
        characters_sum = sum([ord(letter) for letter in cool_emoji])
        if characters_sum > cool_threshold_sum:
            print("".join(emoji[0]))


text = input()
cool_threshold = found_cool_threshold(text)
found_emojis(text, cool_threshold)
