f = open("New4.txt" , "r")       # создает новый файл если этот не существует
# f.write("\nHello \nWorld")           # записывает в файл данные
a = f.readlines()
print(a[1])
f.close()



