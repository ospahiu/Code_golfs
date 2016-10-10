# Returning flattened list in arbitrary nested list challenge.
# Link -> http://codegolf.stackexchange.com/questions/80096/flatten-the-array

from itertools import *
# Golf:
f=lambda x:not isinstance(x,list)and[x]or sum(map(f,x),[])
print f([1,2,4,[1,3,[2]]])

# Non-golfed
def f(seq):
    if isinstance(seq, list):
        accum = []
        for e in seq:
            accum += f(e)
        return accum
    else:
        return [seq]
print f([1,2,4,[1,3,[2]]])


