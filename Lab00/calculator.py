class rpnCalculator:
    'this is my calculator'

    def __init__(self):
        self.memory = []
  
    def pushValue(self, value):
        self.memory.append(value)
        print "pushed value: %d" %value

    def popValue(self):
        return self.memory.pop()

    def add(self):
        x=self.memory.pop()
        y=self.memory.pop()
        z=x+y
        self.memory.append(z)

        
