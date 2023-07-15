import re

sentence = input()
valid_links = []
pattern = r"(w{3}.[a-zA-Z0-9-\.]+\.[a-z]+)"
while sentence:
    matches = re.search(pattern, sentence)    # matches = re.findall(pattern, sentence)
    if matches:
        valid_links.append(matches.group(1))    # valid_links.append(matches[0])
    sentence = input()
for link in valid_links:
    print(link)
