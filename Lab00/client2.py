from socket import *
from pickle import *

s=socket()
host=gethostname()
port=1222
s.connect((host,port))

s.send('15')
msg = s.recv(1024)
serv = loads(msg)
print serv.value
s.close
