import re


def extract_title_and_content(html_string):
    title_pattern = r"<title>(.*?)<\/title>"
    title_match = re.search(title_pattern, html_string)
    title = title_match.group(1) if title_match else ""

    body_pattern = r"<body>(.*?)<\/body>"
    body_match = re.search(body_pattern, html_string)
    content = body_match.group(1) if body_match else ""
    clean_content = re.sub(r"<[^<]+>", "", content).replace("\\n", "")

    return title.strip(), clean_content.strip()


html_text = input()

title, content = extract_title_and_content(html_text)

print(f"Title: {title}")
print(f"Content: {content}")
