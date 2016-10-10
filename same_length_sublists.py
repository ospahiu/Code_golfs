# Check if nested 2D nested list has same length list elements.
# Link -> http://codegolf.stackexchange.com/questions/82503/same-length-sub-arrays

f=lambda x:all(len(i)==len(x[0])for i in x)if x else x
f=lambda x:len(set(map(len,x)))==1 if x else None
f=lambda x:len(set(map(len,x)))<2 if x else None
f=lambda x:x and len(set(map(len,x)))<2

all_lists = []
print "List: {} - {}".format(all_lists, f(all_lists))
all_lists = [[1],[1], [2]]
print "List: {} - {}".format(all_lists, f(all_lists))
all_lists = [[1]]
print "List: {} - {}".format(all_lists, f(all_lists))
all_lists = [[1,2,3,4]]
print "List: {} - {}".format(all_lists, f(all_lists))
all_lists = [[1,2,3,4,5] , [2], [12,314123]]
print "List: {} - {}".format(all_lists, f(all_lists))
all_lists = [[1,2,3,4], [1]]
print "List: {} - {}".format(all_lists, f(all_lists))