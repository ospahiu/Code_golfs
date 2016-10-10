# Answer to -> http://codegolf.stackexchange.com/questions/89241/be-respectful-in-the-restroom#89241 
import itertools

# Non-golf
def find_furthest_stall(input_string):
	input_string = input_string
	a = [not bool(int(i)) for i in input_string]
	y = {i : item for i, item in enumerate(a)}
	d = {i : abs(i[0]-i[1]) for i in list(itertools.combinations(y.keys(), 2))}

	largest = [0,0]
	for key, value in d.iteritems():
		if value >= largest[1] and (y[key[0]] or y[key[1]]):
			largest[0] = key[0] if y[key[0]] else key[1] 
			largest[1] = value

	stall_pipe = '|' + '|'.join(['-' if int(i) else ' ' for i in input_string]) + '|'
	print('Input:\n{} OR {}'.format(stall_pipe, input_string))
	print('Output:\n{}\n'.format(largest[0]))

# Test out.
for sequence in ['101', '001011', '101000011', '100000110000', '11110000001', '10', '10100']: 
	find_furthest_stall(sequence)

# Golfed
y={i:j for i,j in enumerate(not bool(int(i))for i in'100000110000')}
d={i:abs(i[0]-i[1])for i in list(itertools.combinations(y.keys(),2))}
q=[0,0]
for k,v in d.iteritems():
	if v>=q[1]and(y[k[0]]or y[k[1]]):q[0]=k[0]if y[k[0]]else k[1];q[1]=v

print('Largest -> {}'.format(q[0]))




