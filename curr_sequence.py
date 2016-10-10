# Curr sequence golf attempts.

# 1st Attempt
def c(n):A=[n];exec'A=sum([range(1,j+1)for j in A],[]);'*n;print A
c(3)

# 2nd Golf
f = lambda i:eval("[i "+"for i in range(1,i+1)"*i+"]")
print f(3)

# Non-golfed
def curr(n):
	A = [n]  # Initialize singleton list
	for i in range(n):
		N = []  # Declare sublist for every i natural num
		for j in A:
			A += range(1, j+1)  # Add sublist to N
			A = N  # Make A the new list containaing nth sequence
	return A
print curr(3)