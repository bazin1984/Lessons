from math import *

a = float(input("Введите число a != 0"))
b = float(input("Введите число b"))
c = float(input("Введите число c"))
d = pow(b, 2) - 4 * a * c
if d < 0:
    print("Нет корней")
elif d == 0:
    print(-b / (2 * a))
else:
    x1 = (-b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    print(min(x1, x2))       # выводит наименьшее из значений x1 и x2
    print(max(x1, x2))       # выводит наибольшее из значений x1 и x2


