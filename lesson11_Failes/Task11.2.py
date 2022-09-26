f = open("example.txt" , "r")
print(f.read(5))       # выводит количество символов
print(f.read(5))       # запоминает предыдущую позицию элементов

x = open("text.txt" , "r")       # выводим по одной строке файла
print(x.readline())
print(x.readline())
print(x.readline())
x.close()

x = open("text.txt", "r")       # выводим все строки файла
print(x.readlines())
print(x.readlines())
print(x.readlines())
x.close()