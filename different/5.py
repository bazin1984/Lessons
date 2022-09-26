for i in range(1,101) :
    k = 0
    for u in range(1,i) :
        if i % u == 0 :
            k += 1
    if k == 1 :
        print(i,end=" ")
