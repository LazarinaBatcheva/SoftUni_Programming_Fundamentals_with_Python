title_of_an_article = input()
content_of_article = input()

print(f"<h1>\n      {title_of_an_article}\n</h1>")
print(f"<article>\n     {content_of_article}\n</article>")

comment = input()

while comment != "end of comments":
    print(f"<div>\n     {comment}\n</div>")
    comment = input()