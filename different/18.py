f = open(r"D:\urokipython\lesson11_Failes\1.txt" , "r" , encoding="utf-8")
# print(f.read(3))
# print(f.read(3))
# print(f.seek(0))
# print(f.read(3))
# print(f.seek(0))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.seek(0))
# for i in f :
#     print(i)      #  за одну итерацию получаем одну строку нашего файла
# for row in f :
#     for letter in row :
#         print(letter)

# s = f.readlines()
# print(s)

s2 = f.readline()
s3 = f.readline()
s4 = f.readline()
print(s2)
print(s3)
print(s4)