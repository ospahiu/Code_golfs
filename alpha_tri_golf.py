# Code golf attempt for printing out alpha triangle.
# Link -> http://codegolf.stackexchange.com/questions/87496/alphabet-triangle

# 1st Golf
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"*2
for i in range(51):
	print(s[:-i-1]+s[-i-3::-1],s[:i]+s[i::-1])[26>i]

# 2nd Golf
for i in range(51):
	print s[:i]+s[i::-1]if 26>i else s[:-i-1]+s[-i-3::-1]

# 3rd Golf
l=range(26)
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in l+l[24::-1]:print a[:i]+a[i::-1]

# Non-golfed
import string

def print_alphatriangle(n):
	offset = 1
	tail_offset = 3
	alpha = string.ascii_uppercase * n

	for i in range(len(alpha) - offset):
		if len(alpha) / 2 > i:
			print alpha[:i] + alpha[i::-offset]
			continue
		print alpha[:-i-offset] + alpha[-i-tail_offset::-offset]

print_alphatriangle(2)

# Update to non-golfed version
def print_alphatriangle():
	alpha = string.ascii_uppercase
	l = range(26)
	l = l+l[24::-1]
	for i in l:
		print alpha[:i]+alpha[i::-1]

print_alphatriangle()

