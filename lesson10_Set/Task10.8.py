# исключения

try :                                         # прописываем условие где возможна ошибка
    k = 1 / 0
except ZeroDivisionError :
    k = 0
print(k)

a = {"a" : 1 , "b" : 2 , "d" :4}
try :
    values = a["d"]
except KeyError :
    print("This key doesn't exist")
else:
    print("Ключ такой имеется")
finally:
    print("finally отработал")
print("Ok")
