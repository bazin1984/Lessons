count_strings = 0
with open("New4.txt" , "r") as file :
    for i in file :
        if i[-1] == "\n" :
            i = i[:-1]
        count_strings += 1
        print("Количество символов в " , count_strings , "строке" , len(i))
print("Количество строк=  " , count_strings)

