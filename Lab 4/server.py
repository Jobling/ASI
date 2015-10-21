import Pyro.core
import Pyro.naming

class Client:
    def __init__(self, id):
        self.id = id
        self.group = []
        self.messages = []


class Server:
    def __init__(self, name):
        self.users = []
        self.name = name
        self.userCounter = -1
        Pyro.core.ObjBase.__init__(self)

    def Register(self):
        """ Called by the client before any other """
        userCounter = userCounter + 1
        self.users.append(Client(userCounter))
        return userCounter
    
    def sendMessage(self, clientIdentifier, message):
        """ Called to send a given message from clientIdentifier to (broadcast for now) """
        for user in self.users:
            user.messages.append((clientIdentifier, 0, message))

    def receiveMessage(self, clientIdentifier):
        """When calling this method the client will receive a list of all previously unread 
messages"""
        msgs = list(self.users[clientIdentifier].messages)
        del self.users[clientIdentifier].messages[:]
        return msgs

def main():    
    buc_server = Server('Bucelas')
    Pyro.core.initServer()
    try:
        ns.createGroup(':mail')
    except:
        pass
    daemon = Pyro.core.Daemon()
    daemon.useNameServer(ns)
    try:
        daemon.connect(buc_server, ':mail.Bucelas')
    except:
        pass
    try:
        daemon.requestLoop()
    finally:
        daemon.shutdown(True)

if __name__== '__main__':
    main()
