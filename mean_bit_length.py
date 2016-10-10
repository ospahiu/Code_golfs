# Calculates the average length of bits.
# Link -> http://codegolf.stackexchange.com/questions/80586/mean-bits-an-average-challenge
import math

# 1st Golf
def bitLen(integerNum):
	return int(math.log(integerNum,2)) + 1 # Log base 2 calculates length
def meanBitLength(n):
	# Returns mean bit length, or 1 if n is 0 (base case)
	return (2.0 - 2 ** bitLen(n)) / n + bitLen(n) if n != 0 else 1

# 2nd Golf O(1)
def f(n): 
   return (2.0-2**(int(math.log(n,2))+1))/n+(int(math.log(n,2))+1)if n!=0 else 1
print f(7)
