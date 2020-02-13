import copy

#shallow copy -> copy object and altering copied object will alter original object
a_list = [1,2,3]
b = copy.copy(a_list)
print(a, b)

#deep copy -> copy object and altering copied object will not alter original object
c_list = [2, 3, 5]
d_list = copy.deepcopy(c_list)
