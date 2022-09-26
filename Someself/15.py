from random import *
n = [randint(0,99) for i in range(25)]
print(n)
s = []
for i in n :
    if i % 7 == 0 or i % 3 == 0 :
        s.append(i)
print(s)