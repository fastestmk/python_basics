shopList = ["Apples", "Oranges", "Bananas", "Grapes"]
print(shopList[0:2])
shopList.append("Blueberries")
print(shopList)

#length of list
print(len(shopList))

#change value
shopList[0] = "BlackGrapes"
print(shopList)

#deleting value with index
del shopList[0]
print(shopList)

#removing value by item in list
shopList.remove("Oranges")
print(shopList)

#deleting last item and getting it in list
last_item = shopList.pop()
print(last_item)
print(shopList)

#deleting item in list by index
print(last_item)
print(shopList)

# #max, min of values in list
# num_list = [1, 4, 2, 1, 6]
# print(max(num_list))
# print(min(num_list))

# my_list = [1, 2, 4, 5]
# new_list = [2, 3]
# my_list.extend(new_list)
# my_list.append([7, 8, 9])
# print(my_list)

q = []
q.append((1,2,4))
q.append((3,4,5))
print(q)
n = q.pop(0)
print(n)
print(q)