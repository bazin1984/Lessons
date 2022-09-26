from math import *

a = float(input("Введите число a"))
b = float(input("Введите число b"))
arif = (a + b) * 0.5
geom = sqrt(a * b)
garm = 2 * a * b * pow((a + b), -1)
quadr = sqrt((pow(a, 2) + pow(b, 2)) * 0.5)
print(arif, geom, garm, quadr, sep="\n")        # sep="\n" - Вывести в отдельных строчках




