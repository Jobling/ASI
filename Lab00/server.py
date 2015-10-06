from socket import *
from calculator import *

s=socket()
calc=rpnCalculator()

host=gethostname()
port=1222

s.bind((host, port))
s.listen(5)
c, addr=s.accept()
print 'Connection from', addr

while True:
    cmd0 = c.recv(1024)
    cmd=cmd0.split(' ')

    if cmd[0]=='push':
        calc.pushValue(int(cmd[1]))
    elif cmd[0]=='pop':
        c.send(str(calc.popValue()))
    elif cmd[0]=='add':
        calc.add()
    elif cmd[0]=='exit':
        break
    

c.close()
