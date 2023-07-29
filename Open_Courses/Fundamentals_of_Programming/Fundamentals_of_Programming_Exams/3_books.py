book = input()
book_store = dict()
sold_books = []

while book != "on work":
    title, author, price, *args = book.split()
    try:
        if float(price) > 0:
            chapters = book.split(" -> ")
            book_store[title] = {}
            book_store[title]["author"] = author
            book_store[title]["price"] = float(price)
            book_store[title]["chapters"] = chapters[1].split(", ")
    except ValueError:
        pass
    book = input()

wanted_book = input()
while wanted_book != "end work":
    if wanted_book in book_store:
        sold_books.append(wanted_book)
    else:
        print("No such book here")
    wanted_book = input()

if sold_books:
    total_sum = 0
    for book in sold_books:
        print(f"SOLD: {book} with author {book_store[book]['author']}. "
              f"Chapters in the book {len(book_store[book]['chapters'])}")
        total_sum += book_store[book]["price"]
    print(f"Money: {total_sum:.2f}")
else:
    print("Bad day :(")