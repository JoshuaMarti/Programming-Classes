books = []
subBooks = []
chapterCount = []
bookSelection = input('Enter "Old Testament", "New Testament", "Book of Mormon", "Doctrine and Covenants", or "Pearl of Great Price"\n\t-->')
while bookSelection != "Old Testament" and bookSelection != "New Testament" and bookSelection != "Book of Mormon" and bookSelection != "Doctrine and Covenants" and bookSelection != "Pearl of Great Price":
    bookSelection = input('Enter "Old Testament", "New Testament", "Book of Mormon", "Doctrine and Covenants", or "Pearl of Great Price"\n\t-->')
with open("books_and_chapters.txt") as inputFile:
    for line in inputFile:
        line = line.strip()
        ingest = line.split(":")
        subBooks.append(ingest[0])
        chapterCount.append(int(ingest[1]))
        books.append(ingest[2])
        if ingest[2] == bookSelection:
            print(f"Scripture: {ingest[2]}, Book: {ingest[0]}, Chapters: {ingest[1]}")
maxChapters = 0
maxChapterSpot = 0
for spot in range(len(books)):
    if chapterCount[spot] > maxChapters and books[spot] == bookSelection :
        maxChapters = chapterCount[spot]
        maxChapterSpot = spot
print(f"The book with the greatest number of chapters is {subBooks[maxChapterSpot]} in the {books[maxChapterSpot]} with {maxChapters} chapters.")

