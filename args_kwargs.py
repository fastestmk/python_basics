def arg(*args):
	for i in args:
		print(i, end = " ")

def kwarg(**kwargs):
	for i in kwargs:
		print(i, end = " ")
if __name__ == '__main__':
	arg(1,2,4,5)
	print()		
	kwarg(a=3,b=5,c=2)