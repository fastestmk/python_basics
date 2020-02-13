class Person:

	stream = 'cse' # class variable

	# this is constructor, it is run as soon as an object of class is created
	def __init__(self, name, age): 
		# instance variable:variables whose value is assigned inside a constructor or method with self
		self.name = name 
		self.age = age

	def getName(self):
		print("your name is " + self.name)
	def getAge(self):
		print(self.age)	

obj = Person("bob", 12)
obj.getAge()
obj.getName()
print(obj.stream)