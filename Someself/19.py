# Найти все простые числа в диапазоне [0;99]
for i in range(1,100) :
    k = 0
    for u in range(1,i + 1) :
        if i % u == 0 :
            k += 1
    if k == 2 :
        print(i,end=" ")


