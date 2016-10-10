# Permutations of leters challenge.

import itertools

# 1st Golf
r=[]
def f(m,s,t):exec("if s>=1:\n for i in m:f(m,s-1,t+i)\nelse:r.append(t)");return r  # @Olsi Spahiu

# 2nd Golf
def f(m,s): print [''.join(i) for i in itertools.product(m, repeat=s)]  # Using itertools

# Non-golfed
result = []
def f(m, s, total=''):
    if s >= 1:
        for i in m:
            f(m,s-1,total+i)
    else:
		  result.append(total)
    return result

print f('abc', 2)

