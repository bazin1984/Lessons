f = open("example.txt" , "r")
# fp = open("C: xyz.txt" , "r")      # поиск файла в другой дериктории
print(*f)    #  выводит содержимое
print(f)      #   выводит обьект
f.close()      #  закрытие файла

f = open("example.txt" , "r")       # альтернативный метод закрытия файла
try :
    print(*f)
finally:
    f.close()

with open("example.txt") as f :   # инструкция with после работы с файлом автоматически закроет
    print(*f)                                   # его после того как уберем табуляцию.

