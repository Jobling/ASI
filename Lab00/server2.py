from socket import *
from testPickle import *
from pickle import *

s=socket()
host=gethostname()
port=1222

s.bind((host, port))
s.listen(5)

while True:
    c, addr=s.accept()
    print 'Connection from', addr

    value = int(c.recv(1024))
    serv = testClass(value)
    print(dumps(serv))
    c.send(dumps(serv))    
    c.close()
