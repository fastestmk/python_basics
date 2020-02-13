# students = {"Bob": 12, "Rachel": 15, "Anu": 14}
# print(students["Bob"])

#length of dictionary
# print(len(students))

#updating values
# students["Rachel"] = 13
# print(students)

#deleting values
# del students["Anu"]
# print(students)

my_dict = {'age': 24, 'country':'India', 'pm':'NAMO'}
for key, val in my_dict.items():
	print("My {} is {}".format(key, val))	
for key in my_dict:
	print(key)
for val in my_dict.values():
	print(val)