with open("books.txt") as bookFile:
    print("With end behaviour")
    for book in bookFile:
        print(book, end="")
    print("With strip")
with open("books.txt") as bookFile:    
    for boo2k in bookFile:
        book = boo2k.strip()
        print(book)