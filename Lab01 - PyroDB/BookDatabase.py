import pickle
from book import *

class database:
    'This is a book database'
    def __init__(self):
        try:
            f = open("database.dump", "r")
            aux = pickle.load(f)
            self.shelf = aux.shelf
            self.identifier = aux.identifier
            f.close()
        except Exception:
            self.shelf = []
            self.identifier = 0

    def insertBook(self, title, author):
        for b in self.shelf:
            if b.title, b.author == title, author:
                print 'Livro ja existente'
                return

        bid = self.identifier
        self.identifier += 1

        new_book = book(author, title, bid)
        self.shelf.append(new_book)

        f = open("database.dump", "w")
        pickle.dump(self, f)
        f.close()

    def showBook(self, identifier):
        for obj in self.shelf:
            if obj.bid == identifier:
                return obj
        return 'No such book in this shelf!'

    def listBooks(self, Author):
        objList()
        for obj in self.shelf:
            if obj.Author == Author:
                objList.append(obj)
        return objList

    
     
