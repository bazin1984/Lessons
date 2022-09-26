# 3. Напишите программу, демонстрирующую работу try\except\finally.

names = {
    "Alex" : "38 years old" ,
    "Sam" : "49 years old",
    "Jack" : "32 years old"
}

try :
    keys = input("Введите Имя  :   ")
    print(names[keys])
except KeyError :
    print("Введенного имени нет в словаре , необходимо добавить данные")
    names[input("Введите имя    ")] = input("Введите данные    ")
finally:
    print(names)
    print("Работа завершена")
