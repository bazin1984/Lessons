s = {1,2,3,4,5,6}
f = frozenset((5,6,7,8,9))
print(s | f)
print(s&f)
a = {3,4,5,6,7,8,9}
print(a)
print(a.intersection(s))
print(a.intersection_update(s))
print(a)

