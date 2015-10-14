#!/usr/bin/env python

from BookDatabase import *
import Pyro.core
import Pyro.naming

class remoteLibrary(Pyro.core.ObjBase, database):
    def __init__(self, name):
        Pyro.core.ObjBase.__init__(self)
        database.__init__(self, name)

def main():

    db = remoteLibrary('Bucelas')
    Pyro.core.initServer()

    locator = Pyro.naming.NameServerLocator()
    ns = locator.getNS()
    print ns
    
    try:
        ns.createGroup(':libraries')
    except:
        pass

    daemon = Pyro.core.Daemon()
    daemon.useNameServer(ns)

    try:
        daemon.connect(db, ':libraries.Bucelas')
    except:
        pass

    try:
        daemon.requestLoop()
    finally:
        daemon.shutdown(True)

if __name__== '__main__':
    main()
