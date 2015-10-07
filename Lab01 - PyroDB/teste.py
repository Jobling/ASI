from BookDatabase import *

Base = database()
Base.insertBook("Harry Potter", "J. K. Rowling")
Base.insertBook("Crepusculo", "Stephanie Meyer")
Base.insertBook("Memorial do Convento", "Jose Saramago")

for b in Base.shelf:
    print b.Title, b.Author, str(b.bid)
