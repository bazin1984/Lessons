x1 = "123456789"
x2 = "zxcvbnmasdfghjklqwertyuiop"
x3 = x2.upper()
x4 = ",./<>?;':[]\{}|()-=_+*&^%$#@"
s = x1 + x2 + x3 + x4
x = list(s)
from random import *
shuffle(x)
password = ''.join([choice(x) for i in range(10)])
print(password)
print(type(password))