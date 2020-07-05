from __future__ import division
from sympy import *
from Vector import Vector
from VectorOperator import VectorOperator
from CalculusOperator import CalculusOperator
vOperator = VectorOperator()
cOperator = CalculusOperator()
x,y,z = Symbol('x'), Symbol('y'), Symbol('z')


v1=Vector( str(raw_input("x1: ")) , str(raw_input("y1: ")) , str(raw_input("z1: "))  )
v1.show()
v2=Vector( str(raw_input("x2: ")) , str(raw_input("y2: ")) , str(raw_input("z2: "))  )
v2.show()

print "Cross Product: "
vOperator.cross3d(v1,v2).show()
print "Dot Product: "
print vOperator.dot(v1,v2)

print v1.getUnit().getMagnitude()

vOperator.gradient("x^2*y*z").show()

