

# li = ['1','2','3','4','5']

# s = 'aaa bbb ccc ddd'
# ans = '_'.join(li)
# res = li.split('/')
# # res = '_#'.join(li)
# print(ans)
# print(res)

# word = 'geeks,for:geeks'
# print(word.split(','))

# towns = [{'name': 'Manchester', 'population': 58241}, 
# 		{'name': 'Coventry', 'population': 12435}, 
# 		{'name': 'South Windsor', 'population': 25709}]


# class Parent:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print('this is parent class')

# 	def get_name_age(self):
# 		print('your name is {} and your age is {}'.format(self.name, self.age))	

# class Child:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print('this is child class')


# 	def get_name_age(self):
# 		print('your name is {} and your age is {}'.format(self.name, self.age))	

# obj = Parent('sdf', 213)
# obj = Child('asdf', 215)
# print(obj.get_name_age())


# def duplicate(num_list):
# 	visited = [0]*len(num_list)
# 	for num in num_list:
# 		if visited[num] == 0:
# 			visited[num] = 1
# 		else:
# 			return 'true'
# 	return 'false'		

# if __name__ == '__main__':
# 	num_list = [1,2,3,4]
# 	print(duplicate(num_list))

# def twosum(arr, sum):
# 	hash = {}
# 	for i, a in enumerate(arr):
# 		if sum-a in hash:
# 			return hash[sum-a]+1, i+1
# 		hash[a] = i
# 	return [-1,-1]

# def twosum(arr, sum):
# 	hash = {}
# 	for i, a in enumerate(arr):
# 		if sum-a in hash:
# 			return hash[sum-a], i
# 		hash[a] = i	
# if __name__ == '__main__':
# 	arr = [int(i) for i in input().split()]
# 	sum = int(input())
# 	print(twosum(arr, sum))

# q = []
# q.append((1,2,4))
# q.append((3,4,5))
# n = q.pop(0)
# print(n)
# print(q)

# name = "Manoj Kumar"
# n = len(name)
# reverse_name = ''
# for i in range(n-1, -1, -1):
# 	reverse_name += name[i]
	
# print(reverse_name)

urls.py

urlpatterns = [
	path('', view_name, name=''),
	path('<str:slug>', view_name.as_view(), name='')
]