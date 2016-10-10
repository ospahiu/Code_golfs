# Check frequency of parallel lists.

def freq(var):
	d = {} 
	# Initialize dictionaries.
	for c,i in enumerate(reversed(var)): 
		d={ k : 0 for k in set(i) } if c == 0 else { k : d.copy() for k in set(i) }
	# Check for frequency.
	for i ,j in zip(*var):
		for val in d[i]:
		 	if val == j:
		 		d[i][val] +=1
	return d

print( freq((['a','b','b','c'],['one','two','two','two'])) )
