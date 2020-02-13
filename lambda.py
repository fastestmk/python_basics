square = lambda x : x**2
print(square(2))

#map with lambda
li = [2, 3, 5, 4]
squares = list(map(lambda x : x**2, li))
print(squares)

#filter with lambda
odd = list(filter(lambda x : x%2!=0, li))
print(odd)