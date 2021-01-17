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
		self.resolveFormat()
    

	def resolveFormat(self):
		if(type(self.x)==str and getType(self.x)==float):
			self.x = float(self.x)
		if(type(self.y)==str and getType(self.y)==float):
    			self.y = float(self.y)
		if(type(self.z)==str and getType(self.z)==float):
    			self.z = float(self.z)

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

	
	def scale(self,num):
		if(isinstance(num,(int,float))):
			if(isinstance(self.x,(int,float))):
				self.x*=num
			else:
				self.x=self.cOperator.multiply(self.x,num)
			if(isinstance(self.y,(int,float))):
				self.y*=num
			else:
				self.y=self.cOperator.multiply(self.y,num)
			if(isinstance(self.z,(int,float))):
				self.z*=num
			else:
				self.z=self.cOperator.multiply(self.z,num)
		else:
			self.x=self.cOperator.multiply(self.x,num)
			self.y=self.cOperator.multiply(self.y,num)
			self.z=self.cOperator.multiply(self.z,num)
	
	def add(self,other):
		if(isinstance(self.x,(int,float)) and isinstance(other.x,(int,float))):
			self.x += other.x
		else:
			self.x=self.cOperator.add(self.x,other.x)
		if(isinstance(self.y,(int,float)) and isinstance(other.y,(int,float))):
    			self.y += other.y
		else:
			self.y=self.cOperator.add(self.y,other.y)
		if(isinstance(self.z,(int,float)) and isinstance(other.z,(int,float))):
    			self.z += other.z
		else:
			self.z=self.cOperator.add(self.z,other.z)
		
	def subtract(self,other):
		if(isinstance(self.x,(int,float)) and isinstance(other.x,(int,float))):
			self.x -= other.x
		else:
			self.x=self.cOperator.subtract(self.x,other.x)
		if(isinstance(self.y,(int,float)) and isinstance(other.y,(int,float))):
			self.y -= other.y
		else:
			self.y=self.cOperator.subtract(self.y,other.y)
		if(isinstance(self.z,(int,float)) and isinstance(other.z,(int,float))):
			self.z -= other.z
		else:
			self.z=self.cOperator.sub(self.z,other.z)
	def multiply(self,other):
		if(isinstance(self.x,(int,float)) and isinstance(other.x,(int,float))):
			self.x *= other.x
		else:
			self.x=self.cOperator.multiply(self.x,other.x)
		if(isinstance(self.y,(int,float)) and isinstance(other.y,(int,float))):
			self.y *= other.y
		else:
			self.y=self.cOperator.multiply(self.y,other.y)
		if(isinstance(self.z,(int,float)) and isinstance(other.z,(int,float))):
			self.z *= other.z
		else:
			self.z=self.cOperator.multiply(self.z,other.z)

	def divide(self,other):
		if(isinstance(self.x,(int,float)) and isinstance(other.x,(int,float))):
			self.x /= other.x
		else:
			self.x=self.cOperator.divide(self.x,other.x)
		if(isinstance(self.y,(int,float)) and isinstance(other.y,(int,float))):
			self.y /= other.y
		else:
			self.y=self.cOperator.divide(self.y,other.y)
		if(isinstance(self.z,(int,float)) and isinstance(other.z,(int,float))):
			self.z /= other.z
		else:
			self.z=self.cOperator.divide(self.z,other.z)
			
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


def getType(num):
	try:
		float(num)
		return float
	except:
		return str