# multiple input using list comprehension
# a, b, c = [int(i) for i in input().split()]
# print(a, b, c)

# List as input using list comprehension
# my_list = [int(i) for i in input().split()]
# print(my_list)
# for x in my_list:
	# print(x, end=" ")

# 4*4 Matrix as input
# matrix = [[int(j) for j in input().split()] for i in range(4)]

# seq = [2, 3, 5, 1, 6, 7, 8]
# squares_of_even = [i**2 for i in seq if i%2==0]
# print(squares_of_even)

# charlist =  ['A', 'B', 'C']
# ans = [x.lower() for x in charlist]
# print(ans)


# s = 'aaa bbb ccc ddd'
# print(''.join(s.split()))

# s = 'aaa bbb ccc ddd'
# s1 = str(''.join([i for i in s if i != ' ']))
# s2 = [i for i in s if i != ' ']
# print(s1)
# print(s2)

# li = [1, 2, 4, 0, 3]
# print_dict = {i:i*i for i in li}
# print(print_dict) 
# print_list = [[i,i*i] for i in li]
# print(print_list)

word = 'CatBatSatFatOr'
print([word[i:i+3] for i in range(len(word))])
print([word[i:i+3] for i in range(0, len(word), 3)])

# towns = [{'name': 'Manchester', 'population': 58241}, 
# 		{'name': 'Coventry', 'population': 12435}, 
# 		{'name': 'South Windsor', 'population': 25709}]

# town_names = []
# for town in towns:
#     town_names.append(town.get('name'))
# print(town_names)    

# # List comprehensions...
# town_names = [town.get('name') for town in towns]
# print(town_names)

# # Map function...
# town_names = map(lambda town: town.get('name'), towns)	
# print(town_names)

# # For loops...
# town_names = []
# town_populations = []
# for town in towns:
#     town_names.append(town.get('name'))
#     town_populations.append(town.get('population'))
# print(town_names)
# print(town_populations)

# # List comprehensions...
# town_names = [town.get('name') for town in towns]
# town_populations = [town.get('population') for town in towns]
# print(town_names)
# print(town_populations)

# # Zip function...
# town_names, town_populations = zip(*[(town.get('name'), town.get('population')) for town in towns])	
# print(town_names)
# print(town_populations)


# # For loops...
# total_population = 0
# for town in towns:
#     total_population += town.get('population')
# # Sum function...
# total_population = sum(town.get('population') for town in towns)
# print(total_population)

# import reduce
# Reduce function...
# total_population = reduce(lambda total, town: total + town.get('population'), towns, 0)

