import math

x = int(input("Введите трехзначное число"))
# x = 100*a + 10*b + c
c = math.fmod(x, 10)
x /= 10
s = math.floor(x)
b = math.fmod(s, 10)
x /= 10
a = math.floor(x)
print(a + b + c)
# можно ли сделать чтобы условия программы не давало ввести число большего порядка?