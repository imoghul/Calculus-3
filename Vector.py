from CalculusOperator import CalculusOperator
from vpython import *
class Vector:

	x,y,z=0,0,0
	
	def __init__(self,xcoor,ycoor,zcoor,original=None):
		self.cOperator = CalculusOperator()
		if(not original==None):
			self.x = original.x
			self.y = original.y
			self.z = original.z
		else:
			self.x=xcoor
			self.y=ycoor
			self.z=zcoor

	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getZ(self):
		return self.z

	def setX(self,xcoor):
		self.x=xcoor
	def setY(self,ycoor):
		self.y=ycoor
	def setZ(self,zcoor):
		self.z=zcoor

	def scaleNum(self,zcoor):
		self.x*=num
		self.y*=num
		self.z*=num
	
	def scale(self,num):
		self.x=self.cOperator.multiply(self.x,num)
		self.y=self.cOperator.multiply(self.y,num)
		self.z=self.cOperator.multiply(self.z,num)

	def getMagnitude(self):
		return self.cOperator.evaluate(self.cOperator.power( ( self.cOperator.addM([self.cOperator.multiply(self.x,self.x),self.cOperator.multiply(self.y,self.y),self.cOperator.multiply(self.z,self.z)])  ),.5))
		
	def getUnit(self):
		return Vector(self.cOperator.divide( self.x,self.getMagnitude()) , self.cOperator.divide(self.y,self.getMagnitude()) , self.cOperator.divide(self.z,self.getMagnitude()))
	
	def show(self):
		print ("<",self.x,", ",self.y,", ",self.z,">")
	def toStr(self):
		return "<",self.x,", ",self.y,", ",self.z,">"
	def toVPython(self):
		return vector(self.x,self.y,self.z)
