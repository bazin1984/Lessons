s = input("Введите текст")
with open("New3.txt" , "w") as file :
    while s != "" :
        file.write(s + '\n')
        s = input("Введите текст   ")
print()



# fail = input("файл :     ")
# f = open(fail , "w")
# while True :
#     s = input("введите данные   ")
#     if s == "" :
#         break
#     f.write(s + "\n")
# f.close()
