# 3. метод sum(a,b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку если переданы нечисловые параметры(например строка)
# примерно такое:

def validate_int_parametrs(func) :
    def wrapper(n,m) :
        try:
            return func(n,m)
        except TypeError :
            print("Error")

    return wrapper

@validate_int_parametrs
def sum(a,b) :
    print(a + b)

sum("khvh",8)