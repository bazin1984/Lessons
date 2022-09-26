# В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.

from  math import *

def circle(r) :
    return pi * pow(r , 2)

def rectangle(a,b) :
    return a * b

def triangle(x,y,z) :
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

choice = input("введите 'k' для рассчета площади круга ,  'p' - прямоугольника ,  't'  - треугольника :      ")

if choice == "k" :
    r = float(input("Введите радиус окружности   "))
    print(f"площадь окружности  S = {circle(r)}")

if choice == "p" :
    a = float(input("Введите первую сторону прямоугольника    "))
    b = float(input("Введите вторую сторону прямоугольника    "))
    print(f"Площадь прямоугольника  S = {rectangle(a,b)}")

if choice == "t" :
    a = float(input("Введите сторону треугольника     "))
    b = float(input("Введите сторону треугольника     "))
    c = float(input("Введите сторону треугольника     "))
    print(f" Площадь треугольника  S = {triangle(a,b,c)}")




