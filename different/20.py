from random import *
s = [randint(-10 , 10) for i in range(20)]
print(s)
a = [0] * 21
for i in s :
    a[i +10] += 1
for i in range(21) :
    if a[i] > 0 :
        print(i - 10 , a[i])
