import sys
from BookDatabase import *

class client:
  'This is a client'

  def __init__(self):
    self.db = database()

  def run(self):
    print 'Command List:'
    print 'NEW - [Title] [Author]'
    print 'SHOW - [Identifier]'
    print 'LIST - [Author]'
    print 'EXIT'

    while True:
      cmd = raw_input('-> ').split()

      # Comando vazio
      if not cmd:
        continue
      
      # Adicionar Livro
      if  cmd[0].upper() == 'NEW':
        if (len(cmd) == 3):
          self.db.insertBook(cmd[1], cmd[2])
        else:
          print 'Title and/or Author missing!'

      # Procurar Identificador  
      elif cmd[0].upper() == 'SHOW':
        if (len(cmd) == 2):
          if (cmd[1].isdigit()):
            b = self.db.showBook(int(cmd[1]))
          else:
            print 'Identifier must be an <int>'
            continue
            
          if type(b) is str:
            print b
          else:
            print 'Title -', b.Title, '| Author -', b.Author
        else:
          print 'Identifier missing!'

      # Procurar por Autor
      elif cmd[0].upper() == 'LIST':
        if (len(cmd) == 2):
          b = self.db.listBooks(cmd[1])
          if type(b) is str:
            print b
          else:
            for b0 in b:
              print 'ID -', b0.bid, '| Title -', b0.Title, '| Author -', b0.Author
              print '-----'
        else:
          print 'Author missing!'
        

      # Sair do programa
      elif cmd[0].upper() == 'EXIT':
        sys.exit(0)

      # Nao e um comando
      else:
        print 'Command not supported!'
      
