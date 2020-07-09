from __future__ import division
from sympy import *

class CalculusOperator:

    def __init__(self):
        x=Symbol('x')
        y=Symbol('y')
        z=Symbol('z')
    def multiply(self,first,second):
		return self.evaluate(("(%s)*(%s)")%(first,second))

    def multiplyM(self,list):
		expr=""
		for i in range(len(list)):
			expr += list[i]
			if (i<len(list)-1):
				expr += "*"

		return self.evaluate(expr)

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

    def plug(self,expression,variables):
        # variables is a 2d array: {{"variables",value},{"variables",value},...}
        for i in variables:
            expression.replace(variables[0],variables[1])
        return simplify(expression)
    def derivative(self,func,differential):
        return diff(func,differential)
    def indefiniteIntegral(self,func,differential):
        return integrate(func)
    def definiteIntegral(self,func,differential,upper,lower):
        return integrate(func,(differential,lower,upper))
    def indefiniteIntegrals(self,func,differentials):
        expr=func
        for i in differentials:
            expr = self.evaluate(integrate(expr,i))
        return expr
    def definiteIntegrals(self,func,differentials):
        # Differential list is 2d array: { {differential, lower, upper} , {differential, lower, upper}, {differential, lower, upper}, ...}
        expr=func
        for i in differentials:
            expr = self.evaluate(integrate(expr,i[0],i[1],i[2]))
        return expr
    