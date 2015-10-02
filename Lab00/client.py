from socket import *

s=socket()

host=gethostname()
port=1222
s.connect((host,port))

while True:
    cmd = raw_input('Push/Pop/Add/Exit --> ')
    s.send(cmd)
    if cmd == 'exit':
        break
    else:
        if cmd=='pop':
            print "result is:", s.recv(1024)
    
s.close

