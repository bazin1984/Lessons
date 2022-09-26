#  Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив
from random import *
arr = [randint(0,5) for i in range(15)]
print(arr)
arr_1 = []
for i in arr :
    if arr.count(i) > 2 :
        if i not in arr_1 :
            arr_1.append(i)
print(arr_1)

