from random import *
a = tuple(randint(0,5) for i in range(10))
b = tuple(randint(-5,0) for u in range(10))
c = a + b
print(c ,'\n',c.count(0))
