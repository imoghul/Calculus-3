from sympy import *

class Vector:

	x,y,z=0,0,0
	
	def __init__(self,xcoor,ycoor,zcoor):
		
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
		
	
	def show(self):
		print "<",self.x,", ",self.y,", ",self.z,">"
	def toStr(self):
		return "<",self.x,", ",self.y,", ",self.z,">"
