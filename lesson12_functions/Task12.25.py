# декоратор

def my_decor(func) :
    def wrapper() :
        print("start")
        func()
        print("end")
    return wrapper

@my_decor
def my_func() :
    print("Тут основная функция")

my_func()

# d = my_decor(my_func)
# d()

