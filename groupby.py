from itertools import groupby

lst = [ {'date':'2008-04-23','value':'1'},
		{'date':'2008-04-01','value':'8'},
		{'date':'2008-04-05','value':'3'},
		{'date':'2009-04-19','value':'5'},
		{'date':'2009-04-21','value':'8'},
		{'date':'2010-09-09','value':'3'},
		{'date':'2010-09-10','value':'4'},]

lst.sort(key=lambda x:x['date'][:7])


# doing groupby by date(only year and month)
# for k, v in groupby(lst, key=lambda x:x['date'][:7]):
# 	print(k, list(v)) # v(value) is list here

# doing groupby by date(only year and month) and summing according to it 
for k, v in groupby(lst, key=lambda x:x['date'][:7]):
	print({'date': k+'-01', 'value': sum(int(d['value']) for d in v )})
