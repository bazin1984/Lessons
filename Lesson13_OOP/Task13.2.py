# Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные задайте статически, две динамически.
# Первая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической переменной во вторую динамическую переменную
# Создайте объект класса.
# Напечатайте обе функции
# Напечатайте переменную a


class Example :
    a = 1                                #  статические переменные, они же явл глобальными для этого класса
    b = 2

    def __init__(self , n , s):     #  создаем динамические переменные n и s
        self.n = n
        self.s = s

    def func(self):
        self.c = 5             #  создаем переменную c
        print(self.c)

    def func_2(self):
        return self.a + self.b

    def func_3(self):
        return self.n ** self.s

example = Example(4,2)        #  создаем обьект(экземпляр класса)


print(example.a)
example.func()
print(example.func_2())
print(example.func_3())










