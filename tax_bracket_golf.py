# Tax bracket golf challenge. Calculate income after federal taxation.
# Canadian tax brackets used.
# Golfed #1 @Olsi Spahiu

# Trivially compute taxbracket.
from bisect import*
f=lambda i,b,r:i-r[bisect(b,i)-1]*i

# Un-golfed
def f(income, tax_bracket, tax_rates):
	l = [j-i for i,j in zip(tax_bracket, tax_bracket[1:]) if income > j]
	l.append(income-tax_bracket[len(l)])
	return income - sum(i*j for i,j in zip(l, tax_rates))

# golfed
def f(c,b,r):
	l=[j-i for i,j in zip(b,b[1:])if c>j]
	return c-sum(i*j for i,j in zip(l+[c-b[len(l)]],r))

brackets = [0,    45282, 90563, 140388, 200000]
rates =    [0.15, 0.205, 0.26,  0.29,   0.33]
print f(250000, brackets, rates)