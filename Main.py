from __future__ import division
from sympy import *
from Vector import Vector
from VectorOperator import VectorOperator
from CalculusOperator import CalculusOperator
vOperator = VectorOperator()
cOperator = CalculusOperator()
x,y,z = Symbol('x'), Symbol('y'), Symbol('z')

# print(cOperator.indefiniteIntegrals(str(input("input function:")),[ [x,2,1] , [y,2,1] , [z,31,2] ]))

# print(cOperator.realTaylorSeries("e^x",x,10,3))
# print ("")
# print (cOperator.approxTaylorSeries("e^x",x,10,3))

# v1=Vector( str(raw_input("x1: ")) , str(raw_input("y1: ")) , str(raw_input("z1: "))  )
# v1.show()
# v2=Vector( str(raw_input("x2: ")) , str(raw_input("y2: ")) , str(raw_input("z2: "))  )
# v2.show()

v=Vector(2,3,1)
v2=Vector(3,0,1)

print(v/2)