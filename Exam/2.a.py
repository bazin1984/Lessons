from math import *
x = float(input("Введите число "))
if (2 * x - pow(x,2)) != 0 :
    a = (1 + x + pow(x,2)) / (2 * x + pow(x,2))
    b = (1 - x + pow(x,2)) / (2 * x - pow(x,2))
    c = 5 - 2 * pow(x,2)
    y = (a + 2 - b) * c
    print(y)
else:
    print("деление на ноль,введите другое число")



