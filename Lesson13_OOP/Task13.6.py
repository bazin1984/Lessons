def decor_pow(func) :
    def wrapper(x,n) :
        return func(x) ** n
    return wrapper

@decor_pow
def f(x) :
    return x

print(f( int(input("Введите число    ")) , int(input("Введите степень     "))))



