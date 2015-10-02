from calculator import *

obj1 = rpnCalculator()
obj1.pushValue(5)
obj1.pushValue(6)
obj1.add()
print "Value = %d" % obj1.popValue()
