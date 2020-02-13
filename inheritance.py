class Parent:
	def __init__(self):
		print("this is the parent class")
	def parentFunc(self):
		print("this is parent function")
	def test(self):
		print("parent")	

class Child(Parent): # inheriting the Parent
	def __init__(self):
		print("this is child class")
	def childFunc(self):
		print("this is child function")	
	def test(self):
		print("child")	

c = Child()
c.childFunc()
c.parentFunc()
c.test() # overriding the parent function if they are same
# p = Parent()
# p.parentFunc()			