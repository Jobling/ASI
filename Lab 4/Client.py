import thread
import time
import Pyro.core
import Pyro.naming

# Global variables
Pyro.core.initClient()
locator = Pyro.naming.NameServerLocator()
ns = locator.getNS()

uri=ns.resolve(':mail.Bucelas')
mail = Pyro.core.getAttrProxyForURI(uri)
Id = mail.Register()

command = []
flag = 0
# Thread functions
def read():
    global flag
    global command
    while True:
        while flag == 0:
            command = raw_input('--> ')
            flag = 1
            
def write():
    while True:
	time.sleep(0.5)
	count +=1
	print "%s" % ( count )

# Main
def main():
    thread.start_new_thread(read, ())
    write()

if __name__ == '__main__':
    main()

    
