from __future__ import division
from sympy import *

class CalculusOperator:

    def __init__(self):
        x=Symbol('x')
        y=Symbol('y')
        z=Symbol('z')
    def multiply(self,first,second):
		return self.evaluate(("(%s)*(%s)")%(first,second))

    def divide(self,first,second):
		return self.evaluate(("(%s)/(%s)")%(first,second))
	
    def add(self,first,second):
		return ("(%s)+(%s)")%(first,second)
    def addM(self,list):
		expr=""
		for i in range(len(list)):
			expr += list[i]
			if (i<len(list)-1):
				expr += "+"

		return self.evaluate(expr)

    def subtract(self,first,second):
		return self.evaluate(("(%s)-(%s)")%(first,second))
    def power(self, base, exp):
        return self.evaluate(("(%s)^(%s)")%(base,exp))

    def evaluate(self,expression):
        return simplify(expression)
    def derivative(self,func,differential):
        return diff(func,differential)
    def indefiniteIntegral(self,func,differential):
        return integrate(func)
    def definiteIntegral(self,func,differential,upper,lower):
        return integrate(func,(differential,upper,lower))