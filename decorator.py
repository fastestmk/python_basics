def main_function(func):
	def anotherFunction(*args, **kwargs):
		print("before function extecution")
		result = func(*args, **kwargs)
		print("after function")
		return result
	return anotherFunction

@main_function
def sum(a,b):
	return a+b

# helloDecorator = main_function(helloDecorator)
print(sum(1,2))


