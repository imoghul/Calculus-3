from __future__ import division
from sympy import *

class CalculusOperator:

    def __init__(self):
        x=Symbol('x')
        y=Symbol('y')
        z=Symbol('z')
        
    def evaluate(self,expression):
        return simplify(expression)
    def derivative(self,func,differential):
        return diff(func,differential)
    def indefiniteIntegral(self,func,differential):
        return integrate(func)
    def definiteIntegral(self,func,differential,upper,lower):
        return integrate(func,(differential,upper,lower))