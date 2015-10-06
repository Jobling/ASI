class rpnCalculator:
  'this is my calculator'

  def __init__(self):
      self.memory = []

  def pushValue(self, value):
    self.memory.append(value)
    print "Pushed value: %d" % value

  def popValue(self):
    if (len(self.memory) < 1):
      x = "null"
    else:
      x=self.memory.pop()
      print "Poped value: %d" % x
    return x

  def add(self):
    if (len(self.memory) < 2):
      print "Nao ha elementos suficientes para somar"
      print "Nenhuma alteracao efectuada"
    else:
        x=self.memory.pop()
        y=self.memory.pop()
        z=x+y
        self.memory.append(z)
		
