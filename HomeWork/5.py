from math import *

AB = int(input("Введите значение стороны AB"))
BC = int(input("Введите значение стороны BC"))
AC = int(input("Введите значение стороны AC"))
if AB + AC > BC and AB + BC > AC and AC + BC > AB:
    print("Треугольник с такими сторонами существует")
    if AB == AC == BC:
        print("Треугольник является равносторонним")
    elif AB == AC or AB == BC or AC == BC:
        print("Треугольник является равнобедренным")
    elif pow(AB,2) == pow(AC,2)+pow(BC,2) or pow(AC,2) == pow(BC,2)+pow(AB,2) or pow(BC,2) == pow(AB,2)+pow(AC,2):
        print("Треугольник является прямоугольным")
    else:
        print("Треугольник является разносторонним")
else:
    print("Треугольник с такими сторонами не существует")       
