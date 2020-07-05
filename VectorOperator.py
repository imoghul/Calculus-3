from __future__ import division
from sympy import *
from Vector import Vector
from CalculusOperator import CalculusOperator
class VectorOperator:

	cOperator=CalculusOperator()

	def __init__(self):
		#x=Symbol('x')
        #y=Symbol('y')
        #z=Symbol('z')
		print "VECTOR OPERATOR intiated"
	

	def dot(self,v1,v2):
		return self.cOperator.evaluate(self.cOperator.add(self.cOperator.add(self.cOperator.multiply(v1.getX(),v2.getX()),self.cOperator.multiply(v1.getY(),v2.getY())),self.cOperator.multiply(v1.getZ(),v2.getZ())))  #(v1.getX()*v2.getX())+(v1.getY()*v2.getY())+(v1.getZ()*v2.getZ())

	def cross3d(self,v1,v2):
		return Vector( self.cOperator.evaluate(self.cOperator.subtract( self.cOperator.multiply(v1.getY(),v2.getZ()) , self.cOperator.multiply(v1.getZ(),v2.getY()) ) ), self.cOperator.evaluate(self.cOperator.subtract( self.cOperator.multiply(v1.getZ(),v2.getX()) , self.cOperator.multiply(v1.getX(),v2.getZ())) ) , self.cOperator.evaluate(self.cOperator.subtract( self.cOperator.multiply(v1.getX(),v2.getY()) , self.cOperator.multiply(v1.getY(),v2.getX())) ) )#v1.getY()*v2.getZ()-v1.getZ()*v2.getY(),v1.getZ()*v2.getX()-v1.getX()*v2.getZ(),v1.getX()*v2.getY()-v1.getY()*v2.getX())
	def cross2d(self,v1,v2):
		return (self.cOperator.subtract( self.cOperator.multiply(v1.getX(),v2.getY()) , self.cOperator.multiply(v1.getY(),v2.getX()) ) )
	def gradient(self,f):

		return Vector(self.cOperator.derivative(f,Symbol('x')),self.cOperator.derivative(f,Symbol('y')),self.cOperator.derivative(f,Symbol('z')))
		