from math import *

x = float(input("Введите значение x"))
x = radians(x)  # Перевели градусы в радианы ( если наоборот , то degrees(x) )
f = sin(x) + cos(x) + pow(tan(x), 2)
print(f)
