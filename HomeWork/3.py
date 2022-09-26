import random

x = random.randint(100, 999)
print(x)
import math

c = math.fmod(x, 10)
x /= 10
s = math.floor(x)
b = math.fmod(s, 10)
x /= 10
a = math.floor(x)
print(a + b + c)
