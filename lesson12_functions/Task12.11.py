# рекурсивные функции

def factorial(n) :
    if n != 0 :
        return n * factorial(n-1)
    return 1
print(factorial(5))

def func(x) : return x

a1 = func   #  присваиваем функции несколько переменных
a2 = a1
print(a1(5))
print(a2(3))
print(func(10))

