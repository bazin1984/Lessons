s = [5,7,6,9,4,8,5,4,7,9,6,5,8,7,4,5,2,6,9,8,7]
a = {}
for i in s :
    a[i] = a.get(i , 0) + 1
for i , u in a.items() :
    print(i ,":", u ,"шт.")