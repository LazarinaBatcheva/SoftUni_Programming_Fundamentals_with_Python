import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
found_mails = re.findall(pattern, sentence)
for mail in found_mails:
    print(mail[0])