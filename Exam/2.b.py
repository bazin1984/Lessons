from math import *
a = float(input("Введите угол a в градусах  "))
b = float(input("Введите угол b в градусах "))
y = float(input("Введите угол y в градусах "))
a = radians(a)
b = radians(b)
y = radians(y)
f = pow(4,-1) * ( sin(a + b - y) + sin(b + y - a) + sin(y + a -b) - sin(a + b + y))
print(f)