from random import *   # Другой способ подключения модуля, можно использовать лишь его методбне надо писать сам модуль
print(random())

print(uniform(5,10))   # Диапазон случайного числа

print(randint(90,100)) # Диапазон случайного целого числа

x = "Привет"
print(choice(x))       # Достаем символ (элемент) из какой-то последовательности
n = [1,66,25,-87,32,-89,25]
print(choice(n))

shuffle(n)             # Перемешивает существующий список
print(n)
                       # Ниже генерируем пароль
str1 = "0123456789"                    # создали строку с набором цифр
str2 = "zxcvbnmlkjhgfdsaqwertyuiop"    # создали строку с набором букв нижнего резистра
str3 = str2.upper()                    # перевели буквы со строки str2 в верхний резистр
print(str1)
print(str2)
print(str3)
str4 = str1 + str2 + str3
print(str4)
lst = list(str4)                       # Создали список из строки str4
shuffle(lst)                           # перемешали символы списка
print(lst)
password = ''.join([choice(lst) for x in range(6)])   # задаем переменную password и задаем
                                                      # на основании имеющихся списков при помощи цикла новый пароль
print(password)
print(type(lst))
print(type(password))