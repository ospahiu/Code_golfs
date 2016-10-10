# Alphabet wave code golf challenge.
# Link -> http://codegolf.stackexchange.com/questions/89283/print-an-alphabet-wave

# 1st Golf
s=map(chr,range(65,91))
for i in range(-26,0):print(s[i]+s[i+1])*13

# 2nd Golf
for i in range(26):print(chr(i+65)+chr(-~i%26+65))*13

# 3rd Golf
i=0;exec'print(chr(i+65)+chr(-~i%26+65))*13;i+=1;'*26

