# Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
# y = x **2  при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# Вычисление значения функции оформить в виде программной функции, которая принимает значение x, а возвращает полученное значение функции (y).

from math import *

def y(x) :
    if -5 <  x <= 5 :
        return pow(x,2)
    if -10 <= x <= -5 :
        return 2 * abs(x) - 1
    if 5 <  x <= 10 :
        return 2 * x
for i in range(-10,11) :
    print(y(i) , end=" ")