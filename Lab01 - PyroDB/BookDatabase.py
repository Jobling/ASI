import pickle
from book import *

class database:
    'This is a book database'
    # Construtor do objecto
    def __init__(self, name):
        self.name = name
        try:
            # Verificacao da existencia de backup da base de dados
            f = open("database" + self.name + ".dump", "r")
            self.shelf = pickle.load(f)
            self.identifier = len(self.shelf)
            f.close()
        except Exception:
            # Caso nao exista, esta e inicializada
            self.shelf = []
            self.identifier = 0

    # Funcao usada paar insercao de um livro na base de dados
    def insertBook(self, title, author):
        # Verificacao se o livro ja existe
        for b in self.shelf:
            if [b.Title, b.Author] == [title, author]:
                print 'Livro ja existente'
                return

        # Se o livro nao existe "cria-se" um identificador para ele 
        bid = self.identifier
        self.identifier += 1

        # Criacao do novo livro
        new_book = book(author, title, bid)
        self.shelf.append(new_book)

        # Criacao de um "backup" da base de dados
        f = open("database" + self.name + ".dump", "w")
        pickle.dump(self.shelf, f)
        f.close()

    # Funcao usada para a pesquisa de um livro por identificador
    def showBook(self, book_id):
        for obj in self.shelf:
            if obj.bid == book_id:
                return obj
        return 'No such book in this shelf!'

    # Funcao usada para a listagem de livros, por autor
    def listBooks(self, Author):
        if not self.shelf:
            return 'There are no books in this database!'
        if Author == '*':
            return self.shelf
        
        objList = []
        for obj in self.shelf:
            if obj.Author == Author:
                objList.append(obj)

        # Como em python a lista vazia tem um valor 'False', pode-se verificar assim a existencia de elementos
        if not objList:
            return 'There are no books with such author.'
        else:
            return objList

    
     
