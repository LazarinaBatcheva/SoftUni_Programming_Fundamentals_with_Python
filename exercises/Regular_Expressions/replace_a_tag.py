import re

data_input = input()
pattern = r"<a href=(.*?)>(.*?)</a>"
while data_input != "end":
    replaced_html_string = re.sub(pattern, r'[URL href=\1]\2[/URL]', data_input)
    print(replaced_html_string)
    data_input = input()