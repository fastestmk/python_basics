players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ] 
scores =  [100, 15, 17, 28, 43 ]

result = zip(players, scores)
result = set(result)
print(result)


for pl, sc in zip(players, scores):
	print("Score of {} is {}".format(pl, sc))

mapped = zip(players, scores)
plyrs, scrs = zip(*mapped) # unzipping
plyrs = list(plyrs) # converting tuples into list
scrs = list(scrs)
print(plyrs)
print(scrs)

